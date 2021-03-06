from django.db import models
from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from longclaw.products.models import ProductVariantBase, ProductBase

class ProductIndex(Page):
    """Index page for all products
    """
    subpage_types = ('catalog.Product', 'catalog.ProductIndex')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)

        if "sort_by" in request.GET:
            sort_by = request.GET.get('sort_by')

            if sort_by[0] == "-":
                context['prod'] = Product.objects.child_of(self).live().annotate(order_products=models.Max(sort_by[1:])).order_by('{}order_products'.format(sort_by[0:1]))
            else:
                context['prod'] = Product.objects.child_of(self).live().annotate(order_products=models.Max(sort_by)).order_by('order_products')
        else:
            context['prod'] = Product.objects.child_of(self).live()
        return context


class Product(ProductBase):
    parent_page_types = ['catalog.ProductIndex']
    description = RichTextField()
    content_panels = ProductBase.content_panels + [
        FieldPanel('description'),
        InlinePanel('images', label='Images'),
        InlinePanel('variants', label='Product variants'),

    ]

    @property
    def first_image(self):
        return self.images.all()


class ProductVariant(ProductVariantBase):
    """Represents a 'variant' of a product
    """
    # You *could* do away with the 'Product' concept entirely - e.g. if you only
    # want to support 1 'variant' per 'product'.
    product = ParentalKey(Product, related_name='variants')
    tax = models.PositiveIntegerField(default=0)

    slug = AutoSlugField(
        separator='',
        populate_from=('product', 'ref','tax'),
        )

    # Enter your custom product variant fields here
    # e.g. colour, size, stock and so on.
    # Remember, ProductVariantBase provides 'price', 'ref' and 'stock' fields
    description = RichTextField()

    @property
    def get_tax(self):
        return self.tax+100

    @property
    def get_tax_value(self):
        return self.tax/100


class ProductImage(Orderable):
    """Example of adding images related to a product model
    """
    product = ParentalKey(Product, related_name='images')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(blank=True, max_length=255)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption')
    ]
