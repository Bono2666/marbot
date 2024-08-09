from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('master/user/', views.user_index, name='user-index'),
    path('master/user/add/', views.user_add, name='user-add'),
    path('master/user/view/<str:_id>/', views.user_view, name='user-view'),
    path('master/user/update/<str:_id>/',
         views.user_update, name='user-update'),
    path('master/user/delete/<str:_id>/',
         views.user_delete, name='user-delete'),
    path('master/user/remove-signature/<str:_id>/',
         views.remove_signature, name='remove-signature'),
    path('master/user/change-password/',
         views.change_password, name='change-password'),
    path('master/user/set-password/<str:_id>/',
         views.set_password, name='set-password'),
    path('master/user-area/view/<str:_id>/',
         views.user_area_view, name='user-area-view'),
    path('master/distributor/', views.distributor_index, name='distributor-index'),
    path('master/distributor/add/', views.distributor_add, name='distributor-add'),
    path('master/distributor/view/<str:_id>/',
         views.distributor_view, name='distributor-view'),
    path('master/distributor/update/<str:_id>/',
         views.distributor_update, name='distributor-update'),
    path('master/distributor/delete/<str:_id>/',
         views.distributor_delete, name='distributor-delete'),
    path('master/area-sales/', views.area_sales_index, name='area-sales-index'),
    path('master/area-sales/add/', views.area_sales_add, name='area-sales-add'),
    path('master/area-sales/view/<str:_id>/',
         views.area_sales_view, name='area-sales-view'),
    path('master/area-sales/update/<str:_id>/',
         views.area_sales_update, name='area-sales-update'),
    path('master/area-sales/delete/<str:_id>/',
         views.area_sales_delete, name='area-sales-delete'),
    path('master/position/', views.position_index, name='position-index'),
    path('master/position/add/', views.position_add, name='position-add'),
    path('master/position/view/<str:_id>/',
         views.position_view, name='position-view'),
    path('master/position/update/<str:_id>/',
         views.position_update, name='position-update'),
    path('master/position/delete/<str:_id>/',
         views.position_delete, name='position-delete'),
    path('master/menu/', views.menu_index, name='menu-index'),
    path('master/menu/add/', views.menu_add, name='menu-add'),
    path('master/menu/view/<str:_id>/', views.menu_view, name='menu-view'),
    path('master/menu/update/<str:_id>/',
         views.menu_update, name='menu-update'),
    path('master/menu/delete/<str:_id>/',
         views.menu_delete, name='menu-delete'),
    path('master/auth/update/<str:_id>/<str:_menu>/',
         views.auth_update, name='auth-update'),
    path('master/auth/delete/<str:_id>/<str:_menu>/',
         views.auth_delete, name='auth-delete'),
    path('master/area-user/delete/<str:_id>/<str:_area>/',
         views.area_user_delete, name='area-user-delete'),
    path('master/cuisine/', views.cuisine_index, name='cuisine-index'),
    path('master/cuisine/add/', views.cuisine_add, name='cuisine-add'),
    path('master/cuisine/view/<str:_id>/',
         views.cuisine_view, name='cuisine-view'),
    path('master/cuisine/update/<str:_id>/',
         views.cuisine_update, name='cuisine-update'),
    path('master/cuisine/delete/<str:_id>/',
         views.cuisine_delete, name='cuisine-delete'),
    path('master/equipment/', views.equipment_index, name='equipment-index'),
    path('master/equipment/add/', views.equipment_add, name='equipment-add'),
    path('master/equipment/view/<str:_id>/',
         views.equipment_view, name='equipment-view'),
    path('master/equipment/update/<str:_id>/', views.equipment_update,
         name='equipment-update'),
    path('master/equipment/delete/<str:_id>/', views.equipment_delete,
         name='equipment-delete'),
    path('master/category/', views.category_index, name='category-index'),
    path('master/category/add/', views.category_add, name='category-add'),
    path('master/category/view/<str:_id>/',
         views.category_view, name='category-view'),
    path('master/category/update/<str:_id>/', views.category_update,
         name='category-update'),
    path('master/category/delete/<str:_id>/',
         views.category_delete, name='category-delete'),
    path('master/package/', views.package_index, name='package-index'),
    path('master/package/add/', views.package_add, name='package-add'),
    path('master/package/view/<str:_id>/',
         views.package_view, name='package-view'),
    path('master/package/update/<str:_id>/',
         views.package_update, name='package-update'),
    path('master/package/delete/<str:_id>/',
         views.package_delete, name='package-delete'),
    path('master/package-rice/<str:_id>/',
         views.package_rice_view, name='package-rice-view'),
    path('master/package-subcuisine/<str:_id>/',
         views.package_subcuisine_view, name='package-subcuisine-view'),
    path('master/package-sidecuisine1/<str:_id>/',
         views.package_sidecuisine1_view, name='package-sidecuisine1-view'),
    path('master/package-sidecuisine2/<str:_id>/',
         views.package_sidecuisine2_view, name='package-sidecuisine2-view'),
    path('master/package-sidecuisine3/<str:_id>/',
         views.package_sidecuisine3_view, name='package-sidecuisine3-view'),
    path('master/package-sidecuisine4/<str:_id>/',
         views.package_sidecuisine4_view, name='package-sidecuisine4-view'),
    path('master/package-sidecuisine5/<str:_id>/',
         views.package_sidecuisine5_view, name='package-sidecuisine5-view'),
    path('master/package-bag/<str:_id>/',
         views.package_bag_view, name='package-bag-view'),
    path('master/package-box/<str:_id>/',
         views.package_box_view, name='package-box-view'),
    path('master/package-addon/<str:_id>/',
         views.package_addon_view, name='package-addon-view'),
    path('master/package-maincuisine/update/<str:_id>/<str:_cuisine>/',
         views.package_maincuisine_update, name='package-maincuisine-update'),
    path('master/package-subcuisine/update/<str:_id>/<str:_cuisine>/',
         views.package_subcuisine_update, name='package-subcuisine-update'),
    path('master/package-sidecuisine1/update/<str:_id>/<str:_cuisine>/',
         views.package_sidecuisine1_update, name='package-sidecuisine1-update'),
    path('master/package-sidecuisine2/update/<str:_id>/<str:_cuisine>/',
         views.package_sidecuisine2_update, name='package-sidecuisine2-update'),
    path('master/package-sidecuisine3/update/<str:_id>/<str:_cuisine>/',
         views.package_sidecuisine3_update, name='package-sidecuisine3-update'),
    path('master/package-sidecuisine4/update/<str:_id>/<str:_cuisine>/',
         views.package_sidecuisine4_update, name='package-sidecuisine4-update'),
    path('master/package-sidecuisine5/update/<str:_id>/<str:_cuisine>/',
         views.package_sidecuisine5_update, name='package-sidecuisine5-update'),
    path('master/package-rice/update/<str:_id>/<str:_cuisine>/',
         views.package_rice_update, name='package-rice-update'),
    path('master/package-bag/update/<str:_id>/<str:_eq>/',
         views.package_bag_update, name='package-bag-update'),
    path('master/package-box/update/<str:_id>/<str:_eq>/',
         views.package_box_update, name='package-box-update'),
    path('master/package-addon/update/<str:_id>/<str:_eq>/',
         views.package_addon_update, name='package-addon-update'),
    path('master/package-maincuisine/delete/<str:_id>/<str:_cuisine>/',
         views.package_maincuisine_delete, name='package-maincuisine-delete'),
    path('master/package-subcuisine/delete/<str:_id>/<str:_cuisine>/',
         views.package_subcuisine_delete, name='package-subcuisine-delete'),
    path('master/package-sidecuisine1/delete/<str:_id>/<str:_cuisine>/',
         views.package_sidecuisine1_delete, name='package-sidecuisine1-delete'),
    path('master/package-sidecuisine2/delete/<str:_id>/<str:_cuisine>/',
         views.package_sidecuisine2_delete, name='package-sidecuisine2-delete'),
    path('master/package-sidecuisine3/delete/<str:_id>/<str:_cuisine>/',
         views.package_sidecuisine3_delete, name='package-sidecuisine3-delete'),
    path('master/package-sidecuisine4/delete/<str:_id>/<str:_cuisine>/',
         views.package_sidecuisine4_delete, name='package-sidecuisine4-delete'),
    path('master/package-sidecuisine5/delete/<str:_id>/<str:_cuisine>/',
         views.package_sidecuisine5_delete, name='package-sidecuisine5-delete'),
    path('master/package-rice/delete/<str:_id>/<str:_cuisine>/',
         views.package_rice_delete, name='package-rice-delete'),
    path('master/package-bag/delete/<str:_id>/<str:_eq>/',
         views.package_bag_delete, name='package-bag-delete'),
    path('master/package-box/delete/<str:_id>/<str:_eq>/',
         views.package_box_delete, name='package-box-delete'),
    path('master/package-addon/delete/<str:_id>/<str:_eq>/',
         views.package_addon_delete, name='package-addon-delete'),
    path('master/channel/', views.channel_index, name='channel-index'),
    path('master/channel/add/', views.channel_add, name='channel-add'),
    path('master/channel/view/<str:_id>/',
         views.channel_view, name='channel-view'),
    path('master/channel/update/<str:_id>/',
         views.channel_update, name='channel-update'),
    path('master/channel/delete/<str:_id>/',
         views.channel_delete, name='channel-delete'),
    path('master/closing-period/', views.closing_index, name='closing-index'),
    path('master/closing-period/add/', views.closing_add, name='closing-add'),
    path('master/closing-period/view/<str:_id>/',
         views.closing_view, name='closing-view'),
    path('master/closing-period/update/<str:_id>/', views.closing_update,
         name='closing-update'),
    path('master/closing-period/delete/<str:_id>/', views.closing_delete,
         name='closing-delete'),
    path('master/division/', views.division_index, name='division-index'),
    path('master/division/add/', views.division_add, name='division-add'),
    path('master/division/view/<str:_id>/',
         views.division_view, name='division-view'),
    path('master/division/update/<str:_id>/',
         views.division_update, name='division-update'),
    path('master/division/delete/<str:_id>/',
         views.division_delete, name='division-delete'),
    path('claim/<str:_tab>/', views.claim_index, name='claim-index'),
    path('claim/add/<str:_area>/<str:_distributor>/<path:_program>/',
         views.claim_add, name='claim-add'),
    path('claim/view/<str:_tab>/<path:_id>/',
         views.claim_view, name='claim-view'),
    path('claim/update/<str:_tab>/<path:_id>/',
         views.claim_update, name='claim-update'),
    path('claim/delete/<str:_tab>/<path:_id>/',
         views.claim_delete, name='claim-delete'),
    path('claim_release/', views.claim_release_index,
         name='claim-release-index'),
    path('claim_release/view/<path:_id>/<int:_is_revise>/',
         views.claim_release_view, name='claim-release-view'),
    path('claim_release/update/<path:_id>/',
         views.claim_release_update, name='claim-release-update'),
    path('claim_release/approve/<path:_id>/',
         views.claim_release_approve, name='claim-release-approve'),
    path('claim_release/return/<path:_id>/',
         views.claim_release_return, name='claim-release-return'),
    path('claim_release/reject/<path:_id>/',
         views.claim_release_reject, name='claim-release-reject'),
    path('claim_archive/', views.claim_archive_index, name='claim-archive-index'),
    path('matrix/claim/', views.claim_matrix_index,
         name='claim-matrix-index'),
    path('matrix/claim/view/<str:_id>/<str:_channel>/',
         views.claim_matrix_view, name='claim-matrix-view'),
    path('matrix/claim/update/<str:_id>/<str:_channel>/<str:_approver>/',
         views.claim_matrix_update, name='claim-matrix-update'),
    path('matrix/claim/delete/<str:_id>/<str:_channel>/<str:_arg>/',
         views.claim_matrix_delete, name='claim-matrix-delete'),
    path('claim_print/<path:_id>/',
         views.claim_print, name='claim-print'),
    path('master/region/', views.region_index, name='region-index'),
    path('master/region/add/', views.region_add, name='region-add'),
    path('master/region/view/<str:_id>/',
         views.region_view, name='region-view'),
    path('master/region/update/<str:_id>/',
         views.region_update, name='region-update'),
    path('master/region/delete/<str:_id>/',
         views.region_delete, name='region-delete'),
    path('master/region-detail/delete/<str:_id>/<str:_area>/',
         views.region_detail_delete, name='region-detail-delete'),
    path('master/customer/', views.customer_index, name='customer-index'),
    path('master/customer/add/', views.customer_add, name='customer-add'),
    path('master/customer/view/<str:_id>/<str:_msg>/',
         views.customer_view, name='customer-view'),
    path('master/customer/update/<str:_id>/',
         views.customer_update, name='customer-update'),
    path('master/customer/delete/<str:_id>/',
         views.customer_delete, name='customer-delete'),
    path('master/customer-detail/update/<str:_id>/<str:_child>/',
         views.customer_detail_update, name='customer-detail-update'),
    path('master/customer-detail/delete/<str:_id>/',
         views.customer_detail_delete, name='customer-detail-delete'),
    path('order/new/<path:_reg>/', views.order_add, name='order-add'),
    path('order/update/<path:_id>/', views.order_update, name='order-update'),
    path('order/child/add/<path:_id>/<int:_add>/',
         views.order_child_add, name='order-child-add'),
    path('order/child/update/<path:_id>/<int:_child>/<int:_add>/',
         views.order_child_update, name='order-child-update'),
    path('order/child/cs/update/<path:_id>/<str:_child>/',
         views.order_child_cs_update, name='order-child-cs-update'),
    path('order/child/delete/<path:_id>/<int:_child>/',
         views.order_child_delete, name='order-child-delete'),
    path('order/child/cs/delete/<path:_id>/<int:_child>/',
         views.order_child_cs_delete, name='order-child-cs-delete'),
    path('order/package/add/<path:_id>/<str:_cat>/<str:_pack>/<str:_type>/<int:_add>/',
         views.order_package_add, name='order-package-add'),
    path('order/package/update/<path:_id>/<int:_package>/<str:_cat>/<str:_pack>/<str:_type>/<int:_add>/',
         views.order_package_update, name='order-package-update'),
    path('order/package/cs/update/<path:_id>/<str:_cat>/<str:_pack>/<str:_type>/',
         views.order_package_cs_update, name='order-package-cs-update'),
    path('order/package/delete/<path:_id>/<int:_package>/',
         views.order_package_delete, name='order-package-delete'),
    path('order/package/cs/delete/<path:_id>/<str:_pack>/',
         views.order_package_cs_delete, name='order-package-cs-delete'),
    path('order/confirm/update/<path:_id>/',
         views.order_confirm_update, name='order-confirm-update'),
    path('order/confirm/<path:_id>/', views.order_confirm, name='order-confirm'),
    path('order/submit/<path:_id>/', views.order_submit, name='order-submit'),
    path('form/', views.form_index, name='form-index'),
    path('order/', views.order_index, name='order-index'),
    path('order/view/<path:_id>/<str:_cat>/<str:_pack>/<str:_type>/<str:_crud>/',
         views.order_view, name='order-view'),
    path('order/cancel/<path:_id>/', views.order_cancel, name='order-cancel'),
    path('order/confirmed/<path:_id>/',
         views.order_confirmed, name='order-confirmed'),
    path('order/cs/update/<path:_id>/<str:_cat>/<str:_pack>/<str:_type>/',
         views.order_cs_update, name='order-cs-update'),
    path('order/cs/child/add/<path:_id>/',
         views.order_cs_child_add, name='order-cs-child-add'),
    path('order/cs/package/add/<path:_id>/<str:_cat>/<str:_pack>/<str:_type>/',
         views.order_cs_package_add, name='order-cs-package-add'),
    path('cashin/', views.cashin_index, name='cashin-index'),
    path('cashin/add/<path:_id>/<str:_msg>/',
         views.cashin_add, name='cashin-add'),
    path('cashin/view/<int:_id>/', views.cashin_view, name='cashin-view'),
    path('cashin/update/<int:_id>/<str:_msg>/',
         views.cashin_update, name='cashin-update'),
    path('cashin/remove-evidence/<int:_id>/',
         views.remove_evidence, name='remove-evidence'),
    path('cashin/delete/<int:_id>/', views.cashin_delete, name='cashin-delete'),
    path('order/invoice/<path:_id>/', views.order_invoice, name='order-invoice'),
    path('order/bap/<path:_id>/', views.order_bap, name='order-bap'),
    path('order/checklist/<path:_id>/',
         views.order_checklist, name='order-checklist'),
]
