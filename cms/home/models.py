from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Collection, Page
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    """
    The Home Page.
    """
    # Hero section of HomePage
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Homepage image'
    )
    hero_text = models.CharField(
        max_length=255,
        help_text='Write an introduction for the bakery',
        default=''
    )
    hero_cta = models.CharField(
        verbose_name='Hero CTA',
        max_length=255,
        help_text='Text to display on Call to Action',
        default=''
    )
    hero_cta_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Hero CTA link',
        help_text='Choose a page to link to for the Call to Action'
    )

    # Welcome section of the homePage
    welcome_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    welcome_text = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Write some promotional copy'
    )
    featured_section_1_icon_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='https://fontawesome.com/v4.7/icons/'
    )
    featured_section_1_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    featured_section_1_text = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text=''
    )
    featured_section_2_icon_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='https://fontawesome.com/v4.7/icons/'
    )
    featured_section_2_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    featured_section_2_text = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text=''
    )
    featured_section_3_icon_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='https://fontawesome.com/v4.7/icons/'
    )
    featured_section_3_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    featured_section_3_text = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text=''
    )
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Featured image'
    )

    # Explore Courses section
    explore_courses_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    explore_courses_text = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Write some promotional copy'
    )
    recommended_course_1_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='the image of first recommended course'
    )
    recommended_course_1_link = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the link of first recommended course'
    )
    recommended_course_1_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the display name of first recommended course'
    )
    recommended_course_1_category = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the category name of first recommended course'
    )
    recommended_course_1_price = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the price of first recommended course'
    )
    recommended_course_2_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='the image of second recommended course'
    )
    recommended_course_2_link = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the link of second recommended course'
    )
    recommended_course_2_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the display name of second recommended course'
    )
    recommended_course_2_category = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the category name of second recommended course'
    )
    recommended_course_2_price = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the price of second recommended course'
    )
    recommended_course_3_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='the image of third recommended course'
    )
    recommended_course_3_link = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the link of third recommended course'
    )
    recommended_course_3_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the display name of third recommended course'
    )
    recommended_course_3_category = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the category name of third recommended course'
    )
    recommended_course_3_price = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the price of third recommended course'
    )
    recommended_course_4_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='the image of fourth recommended course'
    )
    recommended_course_4_link = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the link of fourth recommended course'
    )
    recommended_course_4_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the display name of fourth recommended course'
    )
    recommended_course_4_category = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the category name of fourth recommended course'
    )
    recommended_course_4_price = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the price of fourth recommended course'
    )
    recommended_course_5_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='the image of fifth recommended course'
    )
    recommended_course_5_link = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the link of fifth recommended course'
    )
    recommended_course_5_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the display name of fifth recommended course'
    )
    recommended_course_5_category = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the category name of fifth recommended course'
    )
    recommended_course_5_price = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the price of fifth recommended course'
    )
    recommended_course_6_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='the image of sixth recommended course'
    )
    recommended_course_6_link = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the link of sixth recommended course'
    )
    recommended_course_6_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the display name of sixth recommended course'
    )
    recommended_course_6_category = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the category name of sixth recommended course'
    )
    recommended_course_6_price = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the price of sixth recommended course'
    )
    recommended_course_7_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='the image of seventh recommended course'
    )
    recommended_course_7_link = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the link of seventh recommended course'
    )
    recommended_course_7_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the display name of seventh recommended course'
    )
    recommended_course_7_category = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the category name of seventh recommended course'
    )
    recommended_course_7_price = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the price of seventh recommended course'
    )
    recommended_course_8_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='the image of eighth recommended course'
    )
    recommended_course_8_link = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the link of eighth recommended course'
    )
    recommended_course_8_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the display name of eighth recommended course'
    )
    recommended_course_8_category = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the category name of eighth recommended course'
    )
    recommended_course_8_price = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the price of eighth recommended course'
    )
    more_courses_text = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the text of more courses'
    )
    more_courses_link = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the link of more courses'
    )

    #  Action section
    action_background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='the background image of action'
    )
    benefit_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the title of benefit'
    )
    benefit_text = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the text of benefit'
    )
    action_text = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the text of action'
    )
    action_link = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the link of action'
    )

    # Why us section
    why_us_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the title of why us'
    )
    why_us_text = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the text of why us'
    )
    reason_1_icon_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='https://fontawesome.com/v4.7/icons/'
    )
    reason_1_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    reason_1_text = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text=''
    )
    reason_2_icon_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='https://fontawesome.com/v4.7/icons/'
    )
    reason_2_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    reason_2_text = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text=''
    )
    reason_3_icon_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='https://fontawesome.com/v4.7/icons/'
    )
    reason_3_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    reason_3_text = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text=''
    )
    what_we_offer_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    what_we_offer_text = RichTextField(
        null=True,
        blank=True,
        help_text='Write some promotional copy'
    )
    video_cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='the background image of action'
    )
    video_link = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the link of video'
    )

    # Contact section
    contact_background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='the background image of action'
    )
    contact_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    contact_text = RichTextField(
        null=True,
        blank=True,
        help_text='Write some promotional copy'
    )
    contact_now_text = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the text of action'
    )
    contact_now_link = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='the link of action'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('image'),
            FieldPanel('hero_text', classname="full"),
            MultiFieldPanel([
                FieldPanel('hero_cta'),
                PageChooserPanel('hero_cta_link'),
            ]),
        ], heading="Hero section"),
        MultiFieldPanel([
            MultiFieldPanel([
                FieldPanel('welcome_title'),
                FieldPanel('welcome_text'),
            ]),
            MultiFieldPanel([
                FieldPanel('featured_section_1_icon_name'),
                FieldPanel('featured_section_1_title'),
                FieldPanel('featured_section_1_text'),
            ]),
            MultiFieldPanel([
                FieldPanel('featured_section_2_icon_name'),
                FieldPanel('featured_section_2_title'),
                FieldPanel('featured_section_2_text'),
            ]),
            MultiFieldPanel([
                FieldPanel('featured_section_3_icon_name'),
                FieldPanel('featured_section_3_title'),
                FieldPanel('featured_section_3_text'),
            ]),
            ImageChooserPanel('featured_image'),
        ], heading="Featured sections", classname="collapsible"),
        MultiFieldPanel([
            MultiFieldPanel([
                FieldPanel('explore_courses_title'),
                FieldPanel('explore_courses_text'),
            ]),
            MultiFieldPanel([
                ImageChooserPanel('recommended_course_1_image'),
                FieldPanel('recommended_course_1_link'),
                FieldPanel('recommended_course_1_name'),
                FieldPanel('recommended_course_1_category'),
                FieldPanel('recommended_course_1_price'),
            ]),
            MultiFieldPanel([
                ImageChooserPanel('recommended_course_2_image'),
                FieldPanel('recommended_course_2_link'),
                FieldPanel('recommended_course_2_name'),
                FieldPanel('recommended_course_2_category'),
                FieldPanel('recommended_course_2_price'),
            ]),
            MultiFieldPanel([
                ImageChooserPanel('recommended_course_3_image'),
                FieldPanel('recommended_course_3_link'),
                FieldPanel('recommended_course_3_name'),
                FieldPanel('recommended_course_3_category'),
                FieldPanel('recommended_course_3_price'),
            ]),
            MultiFieldPanel([
                ImageChooserPanel('recommended_course_4_image'),
                FieldPanel('recommended_course_4_link'),
                FieldPanel('recommended_course_4_name'),
                FieldPanel('recommended_course_4_category'),
                FieldPanel('recommended_course_4_price'),
            ]),
            MultiFieldPanel([
                ImageChooserPanel('recommended_course_5_image'),
                FieldPanel('recommended_course_5_link'),
                FieldPanel('recommended_course_5_name'),
                FieldPanel('recommended_course_5_category'),
                FieldPanel('recommended_course_5_price'),
            ]),
            MultiFieldPanel([
                ImageChooserPanel('recommended_course_6_image'),
                FieldPanel('recommended_course_6_link'),
                FieldPanel('recommended_course_6_name'),
                FieldPanel('recommended_course_6_category'),
                FieldPanel('recommended_course_6_price'),
            ]),
            MultiFieldPanel([
                ImageChooserPanel('recommended_course_7_image'),
                FieldPanel('recommended_course_7_link'),
                FieldPanel('recommended_course_7_name'),
                FieldPanel('recommended_course_7_category'),
                FieldPanel('recommended_course_7_price'),
            ]),
            MultiFieldPanel([
                ImageChooserPanel('recommended_course_8_image'),
                FieldPanel('recommended_course_8_link'),
                FieldPanel('recommended_course_8_name'),
                FieldPanel('recommended_course_8_category'),
                FieldPanel('recommended_course_8_price'),
            ]),
            MultiFieldPanel([
                FieldPanel('more_courses_text'),
                FieldPanel('more_courses_link'),
            ]),    
        ], heading="Explore Course sections", classname="collapsible"),
        MultiFieldPanel([
            ImageChooserPanel('action_background_image'),
            FieldPanel('benefit_title'),
            FieldPanel('benefit_text'),
            FieldPanel('action_text'),
            FieldPanel('action_link'),
        ], heading="Action sections", classname="collapsible"),
        MultiFieldPanel([
            MultiFieldPanel([
                FieldPanel('why_us_title'),
                FieldPanel('why_us_text'),
            ]),
            MultiFieldPanel([
                FieldPanel('reason_1_icon_name'),
                FieldPanel('reason_1_title'),
                FieldPanel('reason_1_text'),
            ]),
            MultiFieldPanel([
                FieldPanel('reason_2_icon_name'),
                FieldPanel('reason_2_title'),
                FieldPanel('reason_2_text'),
            ]),
            MultiFieldPanel([
                FieldPanel('reason_3_icon_name'),
                FieldPanel('reason_3_title'),
                FieldPanel('reason_3_text'),
            ]),
            MultiFieldPanel([
                FieldPanel('what_we_offer_title'),
                FieldPanel('what_we_offer_text'),
                ImageChooserPanel('video_cover_image'),
                FieldPanel('video_link'),
            ]),
            MultiFieldPanel([                
                ImageChooserPanel('contact_background_image'),
                FieldPanel('contact_title'),
                FieldPanel('contact_text'),
                FieldPanel('contact_now_text'),
                FieldPanel('contact_now_link'),
            ]),
        ], heading="Contact US sections", classname="collapsible"),
    ]

    def __str__(self):
        return self.title
