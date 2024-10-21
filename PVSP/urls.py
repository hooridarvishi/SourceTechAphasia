# # from django.urls import path
# # from . import views
# # app_name="PVSP"
# # urlpatterns = [
# #     path("", views.home, name='home'),
# # ]
#
# from django.urls import path
# from . import views
#
# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('delete_image/<int:post_id>/', views.delete_image, name='delete_image'),
#     path('delete_post/<int:post_id> /', views.delete_post, name='delete_post'),
# ]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
#
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('delete_post/', views.delete_post, name='delete_post'),
    path('restore_post/', views.restore_post, name='restore_post'),

    path('delete_photo/', views.delete_photo, name='delete_photo'),
    path('restore_photo/', views.restore_photo, name='restore_photo'),

    path('delete_post_second_page/', views.delete_post_second_page, name='delete_post_second_page'),
    path('restore_post_second_page/', views.restore_post_second_page, name='restore_post_second_page'),

    path('delete_photo_second_page/', views.delete_photo_second_page, name='delete_photo_second_page'),
    path('restore_photo_second_page/', views.restore_photo_second_page, name='restore_photo_second_page'),

    path('delete_post_third_page/', views.delete_post_third_page, name='delete_post_third_page'),
    path('restore_post_third_page/', views.restore_post_third_page, name='restore_post_third_page'),

    path('delete_photo_third_page/', views.delete_photo_third_page, name='delete_photo_third_page'),
    path('restore_photo_third_page/', views.restore_photo_third_page, name='restore_photo_third_page'),

    path('delete_photo_forth_page/', views.delete_photo_forth_page, name='delete_photo_forth_page'),
    path('restore_photo_forth_page/', views.restore_photo_forth_page, name='restore_photo_forth_page'),

    path("restore_post_second_step_page_first", views.restore_post_second_step_page_first,
         name="restore_post_second_step_page_first"),
    path("delete_post_second_step_page_first", views.delete_post_second_step_page_first,
         name="delete_post_second_step_page_first"),

    path("restore_photo_second_step_page_first", views.restore_photo_second_step_page_first,
         name="restore_photo_second_step_page_first"),
    path("delete_photo_second_step_page_first", views.delete_photo_second_step_page_first,
         name="delete_photo_second_step_page_first"),

    path("restore_photo_second_step_page_third", views.restore_photo_second_step_page_third,
         name="restore_photo_second_step_page_third"),
    path("delete_photo_second_step_page_third", views.delete_photo_second_step_page_third,
         name="delete_photo_second_step_page_third"),

    path("restore_post_second_step_page_forth", views.restore_post_second_step_page_forth,
         name="restore_post_second_step_page_forth"),
    path("delete_post_second_step_page_forth", views.delete_post_second_step_page_forth,
         name="delete_post_second_step_page_forth"),

    path("restore_photo_second_step_page_forth", views.restore_photo_second_step_page_forth,
         name="restore_photo_second_step_page_forth"),
    path("delete_photo_second_step_page_forth", views.delete_photo_second_step_page_forth,
         name="delete_photo_second_step_page_forth"),
    path("restore_photo_second_step_page_fifth", views.restore_photo_second_step_page_fifth,
         name="restore_photo_second_step_page_fifth"),
    path("delete_photo_second_step_page_fifth", views.delete_photo_second_step_page_fifth,
         name="delete_photo_second_step_page_fifth"),

    path("restore_post_second_step_page_fifth", views.restore_post_second_step_page_fifth,
         name="restore_post_second_step_page_fifth"),
    path("delete_post_second_step_page_fifth", views.delete_post_second_step_page_fifth,
         name="delete_post_second_step_page_fifth"),

    path("second_page", views.second_page, name="second_page"),
    path("third_page", views.third_page, name="third_page"),
    path('', note_list, name='note_list'),
    path("forth_page", views.forth_page, name="forth_page"),

    path("second_step_page_first", views.second_step_page_first, name="second_step_page_first"),
    path("second_step_page_second", views.second_step_page_second, name="second_step_page_second"),
    path("second_step_page_forth", views.second_step_page_forth, name="second_step_page_forth"),

    path("second_step_page_third", views.second_step_page_third, name="second_step_page_third"),
    path("second_step_page_fifth", views.second_step_page_fifth, name="second_step_page_fifth"),
    path("third_step_page_one", views.third_step_page_one, name="third_step_page_one"),

    path("restore_photo_third_step_page_one", views.restore_photo_third_step_page_one,
         name="restore_photo_third_step_page_one"),
    path("delete_photo_third_step_page_one", views.delete_photo_third_step_page_one,
         name="delete_photo_third_step_page_one"),

    path("restore_post_third_step_page_one", views.restore_post_third_step_page_one,
         name="restore_post_third_step_page_one"),
    path("delete_post_third_step_page_one", views.delete_post_third_step_page_one,
         name="delete_post_third_step_page_one"),

    path("third_step_page_two", views.third_step_page_two, name="third_step_page_two"),

    path("restore_photo_third_step_page_two", views.restore_photo_third_step_page_two,
         name="restore_photo_third_step_page_two"),
    path("delete_photo_third_step_page_two", views.delete_photo_third_step_page_two,
         name="delete_photo_third_step_page_two"),

    path("restore_post_third_step_page_two", views.restore_post_third_step_page_two,
         name="restore_post_third_step_page_two"),
    path("delete_post_third_step_page_two", views.delete_post_third_step_page_two,
         name="delete_post_third_step_page_two"),

    path("third_step_page_three", views.third_step_page_three, name="third_step_page_three"),

    path("restore_photo_third_step_page_three", views.restore_photo_third_step_page_three,
         name="restore_photo_third_step_page_three"),
    path("delete_photo_third_step_page_three", views.delete_photo_third_step_page_three,
         name="delete_photo_third_step_page_three"),

    path("restore_post_third_step_page_three", views.restore_post_third_step_page_three,
         name="restore_post_third_step_page_three"),
    path("delete_post_third_step_page_three", views.delete_post_third_step_page_three,
         name="delete_post_third_step_page_three"),
    path("third_step_page_four", views.third_step_page_four, name="third_step_page_four"),
    path("third_step_page_five", views.third_step_page_five, name="third_step_page_five"),
    path("third_step_page_prefour", views.third_step_page_prefour, name="third_step_page_prefour"),
    path('mafool_first_page', views.mafool_first_page, name='mafool_first_page'),
    path("mafool_second_page", views.mafool_second_page, name="mafool_second_page"),
    path("delete_photo_third_step_page_second_mafool", views.delete_photo_third_step_page_second_mafool,
         name="delete_photo_third_step_page_second_mafool"),
    path("restore_photo_third_step_page_second_mafool", views.restore_photo_third_step_page_second_mafool,
         name="restore_photo_third_step_page_second_mafool"),
    path("delete_post_third_step_page_second_mafool", views.delete_post_third_step_page_second_mafool,
         name="delete_post_third_step_page_second_mafool"),
    path("restore_post_third_step_page_second_mafool", views.restore_post_third_step_page_second_mafool,
         name="restore_post_third_step_page_second_mafool"),
    path("mafool_third_page", views.mafool_third_page, name="mafool_third_page"),
    path("mafool_fourth_page", views.mafool_fourth_page, name="mafool_fourth_page"),
    path("delete_photo_third_step_page_fourth_mafool", views.delete_photo_third_step_page_fourth_mafool,
         name="delete_photo_third_step_page_fourth_mafool"),
    path("restore_photo_third_step_page_fourth_mafool", views.restore_photo_third_step_page_fourth_mafool,
         name="restore_photo_third_step_page_fourth_mafool"),
    path("delete_post_third_step_page_fourth_mafool", views.delete_post_third_step_page_fourth_mafool,
         name="delete_post_third_step_page_fourth_mafool"),
    path("restore_post_third_step_page_fourth_mafool", views.restore_post_third_step_page_fourth_mafool,
         name="restore_post_third_step_page_fourth_mafool"),
    path("mafool_fifth_page", views.mafool_fifth_page, name="mafool_fifth_page"),
    path("mafool_sixth_page", views.mafool_sixth_page, name="mafool_sixth_page"),
    path("delete_photo_third_step_page_sixth_mafool", views.delete_photo_third_step_page_sixth_mafool,
         name="delete_photo_third_step_page_sixth_mafool"),

    path("restore_photo_third_step_page_sixth_mafool", views.restore_photo_third_step_page_sixth_mafool,
         name="restore_photo_third_step_page_sixth_mafool"),

    path("delete_post_third_step_page_sixth_mafool", views.delete_post_third_step_page_sixth_mafool,
         name="delete_post_third_step_page_sixth_mafool"),
    path("restore_post_third_step_page_sixth_mafool", views.restore_post_third_step_page_sixth_mafool,
         name="restore_post_third_step_page_sixth_mafool"),
    path("mafool_seventh_page", views.mafool_seventh_page, name="mafool_seventh_page"),
    path("mafool_eighth_page", views.mafool_eighth_page, name="mafool_eighth_page"),

    path("mafool_nineth_page", views.mafool_nineth_page, name="mafool_nineth_page"),

    path("mafool_tenth_page", views.mafool_tenth_page, name="mafool_tenth_page"),

    path("mafool_eleventh_page", views.mafool_eleventh_page, name="mafool_eleventh_page"),

    path("preposition_p_1", views.preposition_p_1, name="preposition_p_1"),
    path("preposition_p_2", views.preposition_p_2, name="preposition_p_2"),
    path("preposition_p_3", views.preposition_p_3, name="preposition_p_3"),
    path("preposition_p_4", views.preposition_p_4, name="preposition_p_4"),
    path("preposition_p_5", views.preposition_p_5, name="preposition_p_5"),
    path("preposition_p_6", views.preposition_p_6, name="preposition_p_6"),
    path("preposition_p_7", views.preposition_p_7, name="preposition_p_7"),
    path("preposition_p_8", views.preposition_p_8, name="preposition_p_8"),
    path("preposition_p_9", views.preposition_p_9, name="preposition_p_9"),
    path("adverb_p_1", views.adverb_p_1, name="adverb_p_1"),
    path("adverb_p_2", views.adverb_p_2, name="adverb_p_2"),

    path("adverb_p_3", views.adverb_p_3, name="adverb_p_3"),

    path("adverb_p_4", views.adverb_p_4, name="adverb_p_4"),
    path("final_p1", views.final_p1, name="final_p1"),
    path('select/', select_images, name='select_images'),
    path('select1/', select_images1, name='select_images1'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
