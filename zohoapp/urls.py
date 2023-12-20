from django.urls import path,include,re_path
from.import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from .views import EmailAttachementView

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('base', views.base, name='base'),
    path('logout', views.logout, name='logout'),
    path('forgotpassword' , views.forgotpassword,name='forgotpassword'),  
    path('setnewpassword' , views.setnewpassword,name='setnewpassword'),   

    path('view_profile', views.view_profile, name='view_profile'),
    path('edit_profile/<pk>', views.edit_profile, name='edit_profile'),
    path('itemview',views.itemview,name='itemview'),
    path('additem',views.additem,name='additem'),
    path('add',views.add,name='add'),
    path('add_account',views.add_account,name='add_account'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('edititem/<int:id>',views.edititem,name='edititem'),
    path('edit_db/<int:id>',views.edit_db,name='edit_db'),
    path('Action/<int:id>',views.Action,name='Action'),
    path('cleer/<int:id>',views.cleer,name='cleer'),
    path('add_unit',views.add_unit,name='add_unit'),
    path('sales',views.add_sales,name='add_sales'),
    path('vendor/',views.vendor,name='vendor'),
    path('add_vendor/',views.add_vendor,name='add_vendor'),
    path('sample/',views.sample,name="sample"),
    path('view_vendor_list/',views.view_vendor_list,name='view_vendor_list'),
    path('view_vendor_details/<int:pk>',views.view_vendor_details,name='view_vendor_details'),
    path('add_comment/<int:pk>',views.add_comment,name='add_comment'),
    path('sendmail/<int:pk>',views.sendmail,name='sendmail'),
    path('edit_vendor/<int:pk>',views.edit_vendor,name='edit_vendor'),
    path('edit_vendor_details/<int:pk>',views.edit_vendor_details,name='edit_vendor_details'),
    path('upload_document/<int:pk>',views.upload_document,name='upload_document'),
    path('download_doc/<int:pk>',views.download_doc,name='download_doc'),
    path('cancel_vendor/',views.cancel_vendor,name='cancel_vendor'),
    path('delete_vendor/<int:pk>',views.delete_vendor,name='delete_vendor'),
    path('add_customer/',views.add_customer,name='add_customer'),
    path('retainer_invoices/',views.retainer_invoice,name='retainer_invoice'),
    path('add_invoice/',views.add_invoice,name='add_invoice'),
    path('create_invoice_draft/',views.create_invoice_draft,name='create_invoice_draft'),
    path('create_invoice_send/',views.create_invoice_send,name='create_invoice_send'),
    path('view_invoice/<int:pk>',views.invoice_view,name='invoice_view'),
    path('retainer_template/<int:pk>',views.retainer_template,name='retainer_template'),
    path('retainer_invoice_edit/<int:pk>',views.retainer_edit_page,name='retainer_edit_page'), 
    path('retainer_invoice_update/<int:pk>',views.retainer_update,name='retainer_update'),
    path('send_mail/<int:pk>',views.mail_send,name='mail_send'),
    path('retaineritem_delete/<int:pk>',views.retaineritem_delete,name='retaineritem_delete'),
    path('retainer_delete/<int:pk>',views.retainer_delete,name='retainer_delete'),
    path('allestimates',views.allestimates,name='allestimates'),
    path('newestimate/',views.newestimate,name='newestimate'),
    path('createestimate/',views.createestimate,name='createestimate'),
    path('itemdata_est/',views.itemdata_est,name='itemdata_est'),
    path('create_and_send_estimate/',views.create_and_send_estimate,name='create_and_send_estimate'),
    path('estimateslip/<int:est_id>',views.estimateslip,name='estimateslip'),
    path('editestimate/<int:est_id>',views.editestimate,name='editestimate'),
    path('updateestimate/<int:pk>',views.updateestimate,name='updateestimate'),
    path('converttoinvoice/<int:pk>',views.converttoinvoice,name='converttoinvoice'),
    path('emailattachment',EmailAttachementView.as_view(),name='emailattachment'),
    path('add_customer_for_estimate/',views.add_customer_for_estimate,name='add_customer_for_estimate'),
    path('entr_custmr_for_estimate/',views.entr_custmr_for_estimate,name='entr_custmr_for_estimate'),
    path('payment_term_for_estimate/',views.payment_term_for_estimate,name='payment_term_for_estimate'),
    path('invoiceview',views.invoiceview,name='invoiceview'),
    path('addinvoice',views.addinvoice,name='addinvoice'),
    path('itemdata',views.itemdata,name='itemdata'),
    path('add_prod',views.add_prod,name='add_prod'),
    path('detailedview/<int:id>',views.detailedview,name='detailedview'),
    path('edited_prod/<int:id>',views.edited_prod,name='edited_prod'),
    path('dele/<int:pk>',views.dele,name='dele'),
    # path('edited/<int:id>',views.edited,name='edited'),
    path('payment_term',views.payment_term,name='payment_term'),
    path('add_cx',views.add_cx,name="add_cx"),
    path('deleteestimate/<int:est_id>',views.deleteestimate,name='deleteestimate'),
    path('additem_est',views.additem_est,name='additem_est'),
    path('additem_page_est',views.additem_page_est,name='additem_page_est'),
    path('add_unit_est',views.add_unit_est,name='add_unit_est'),
    path('add_sales_est',views.add_sales_est,name='add_sales_est'),
    path('add_account_est',views.add_account_est,name='add_account_est'),
    path('customerdata', views.customerdata, name='customerdata'),
    path('add_customer_for_invoice',views.add_customer_for_invoice,name='add_customer_for_invoice'),
    path('payment_term_for_invoice',views.payment_term_for_invoice,name='payment_term_for_invoice'),
    path('addprice',views.addprice,name='addprice'),
    path('addpl',views.addpl,name='addpl'),
    path('viewpricelist',views.viewpricelist,name='viewpricelist'),
    path('viewlist/<int:id>',views.viewlist,name='viewlist'),
    path('editlist/<int:id>',views.editlist,name='editlist'),
    path('editpage/<int:id>',views.editpage,name='editpage'),
    path('delete_item/<int:id>',views.delete_item,name='delete_item'),
    path('active_status/<int:id>',views.active_status,name='active_status'),
    path('createpl',views.createpl,name='createpl'),
    path('banking_home',views.banking_home,name='banking_home'),
    path('create_banking',views.create_banking,name='create_banking'),
    path('save_banking',views.save_banking,name='save_banking'),
    path('view_bank/<int:id>',views.view_bank,name='view_bank'),
    path('banking_edit/<int:id>',views.banking_edit,name='banking_edit'),
    path('save_edit_bnk/<int:id>',views.save_edit_bnk,name='save_edit_bnk'),
    path('save_banking_edit/<int:id>',views.save_banking_edit,name='save_banking_edit'),
    path('save_bank',views.save_bank,name='save_bank'),
    path('banking_delete/<int:id>',views.banking_delete,name='banking_delete'),
    path('entr_custmr',views.entr_custmr,name='entr_custmr'),
    path('get_customer_names', views.get_customer_names, name='get_customer_names'),
    path('expense/delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('get_profile_details/<int:profile_id>/', views.get_profile_details, name='get_profile_details'),
    path('recurringhome',views.recurringhome,name='recurringhome'),
    path('add_expense',views.add_expense,name='add_expense'),
    path('recurringbase',views.recurringbase,name='recurringbase'),
    path('show_recurring/<int:expense_id>/', views.show_recurring, name='show_recurring'),
    # path('expense_details', views.expense_details, name='expense_details'),
    path('edit_expense/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('newexp',views.newexp,name='newexp'),
    path('save-data/', views.save_data, name='save_data'),
    path('get-account-names/', views.get_account_names, name='get_account_names'),
    path('profileshow',views.profileshow,name='profileshow'),
    path('add_customer',views.add_customer,name='add_customer'),
    
    path('view_sales_order',views.view_sales_order,name='view_sales_order'),
    path('create_sales_order',views.create_sales_order,name='create_sales_order'),
    path('add_customer_for_sorder',views.add_customer_for_sorder,name='add_customer_for_sorder'),
    path('payment_term_for_sorder',views.payment_term_for_sorder,name='payment_term_for_sorder'),

    path('add_sales_order',views.add_sales_order,name='add_sales_order'),
    path('sales_order_det/<int:id>',views.sales_order_det,name='sales_order_det'),
    path('edit_sales_order/<int:id>',views.edit_sales_order,name='edit_sales_order'),
    path('delet_sales/<int:id>',views.delet_sales,name='delet_sales'),
    
    path('create_delivery_chellan',views.create_delivery_chellan,name='create_delivery_chellan'),
    path('delivery_chellan_home',views.delivery_chellan_home,name='delivery_chellan_home'),
    path('add_customer_for_challan',views.add_customer_for_challan,name='add_customer_for_challan'),
    path('entr_custmr_for_challan',views.entr_custmr_for_challan,name='entr_custmr_for_challan'),
    path('additem_page_challan',views.additem_page_challan,name='additem_page_challan'),
    path('additem_challan',views.additem_challan,name='additem_challan'), 
    path('delivery_challan_view/<int:id>',views.delivery_challan_view,name='delivery_challan_view'),
    path('delivery_challan_edit/<int:id>',views.delivery_challan_edit,name='delivery_challan_edit'),
    path('update_challan/<int:id>',views.update_challan,name='update_challan'),
    path('create_and_send_challan',views.create_and_send_challan,name='create_and_send_challan'),
    path('create_challan_draft',views.create_challan_draft,name='create_challan_draft'),
    path('get_cust_mail',views.get_cust_mail,name='get_cust_mail'),
    path('additem_edit_challan',views.additem_edit_challan,name='additem_edit_challan'),
    path('additem_challan_edit',views.additem_challan_edit,name='additem_challan_edit'),
    path('add_customer_edit_challan',views.add_customer_edit_challan,name='add_customer_edit_challan'),
    path('sv_cust_edit_challan',views.sv_cust_edit_challan,name='sv_cust_edit_challan'),
    path('add_account_challan_edit',views.add_account_challan_edit,name='add_account_challan_edit'),
    path('add_unit_edit_challan',views.add_unit_edit_challan,name='add_unit_edit_challan'),
    path('add_sales_edit_challan',views.add_sales_edit_challan,name='add_sales_edit_challan'),
    path('payment_term_challan_edit',views.payment_term_challan_edit,name='payment_term_challan_edit'),
    path('payment_term_challan',views.payment_term_challan,name='payment_term_challan'),

    path('add_account_challan',views.add_account_challan,name='add_account_challan'),
    path('add_unit_challan',views.add_unit_challan,name='add_unit_challan'),
    path('add_sales_challan',views.add_sales_challan,name='add_sales_challan'),
    path('render_challan_pdf/<int:id>',views.render_challan_pdf,name='render_challan_pdf'),
    path('deletechallan/<int:id>',views.deletechallan,name='deletechallan'),
    
    path('filter_chellan',views.filter_chellan,name='filter_chellan'),
    path('filter_chellan_type',views.filter_chellan_type,name='filter_chellan_type'),
    path('itemdata_challan',views.itemdata_challan,name='itemdata_challan'),
    path('payment_term_for_sales',views.payment_term_for_sales,name="payment_term_for_sales"),
    
    path('report_page/',views.report_page,name='report_page'),
    path('report_recurring_invoice/',views.report_recurring_invoice,name='report_recurring_invoice'),
    
    path('create_recur',views.create_recur,name='create_recur'),
    path('new_recur',views.new_recur,name='new_recur'),
    path('view_recurpage',views.view_recurpage,name='view_recurpage'),
    path('viewrecur/<int:id>',views.viewrecur,name='viewrecur'),
    path('edit_recur/<int:id>',views.edit_recur,name='edit_recur'),
    path('editrecurpage<int:id>',views.editrecurpage,name='editrecurpage'),
    path('del_recur/<int:del_id>',views.del_recur,name='del_recur'),
    path('itemdata_recur',views.itemdata_recur,name='itemdata_recur'),
    path('payment_recur',views.payment_recur,name='payment_recur'),
    #path('customer_details',views.customer_details,name='customer_details'),
    
    path('recurring_bill',views.recurring_bill,name='recurring_bill'),
    path('recur_custasc',views.recur_custasc,name='recur_custasc'),
    path('recur_custdesc',views.recur_custdesc,name='recur_custdesc'),
    path('recur_vendorasc',views.recur_vendorasc,name='recur_vendorasc'),
    path('recur_vendordesc',views.recur_vendordesc,name='recur_vendordesc'),
    path('recur_profileasc',views.recur_profileasc,name='recur_profileasc'),
    path('recur_profiledesc',views.recur_profiledesc,name='recur_profiledesc'),
    path('add_recurring_bills',views.add_recurring_bills,name='add_recurring_bills'),
    path('create_recurring_bills',views.create_recurring_bills,name='create_recurring_bills'),
    path('edit_recurring_bills/<id>',views.edit_recurring_bills,name='edit_recurring_bills'),
    path('change_recurring_bills/<id>',views.change_recurring_bills,name='change_recurring_bills'),
    path('delete_recurring_bills/<id>',views.delete_recurring_bills,name='delete_recurring_bills'),
    path('view_recurring_bills/<id>',views.view_recurring_bills,name='view_recurring_bills'),
    path('view_custasc/<id>',views.view_custasc,name='view_custasc'),
    path('view_custdesc/<id>',views.view_custdesc,name='view_custdesc'),
    path('view_vendorasc/<id>',views.view_vendorasc,name='view_vendorasc'),
    path('view_vendordesc/<id>',views.view_vendordesc,name='view_vendordesc'),
    path('view_profileasc/<id>',views.view_profileasc,name='view_profileasc'),
    path('view_profiledesc/<id>',views.view_profiledesc,name='view_profiledesc'),
    path('get_vendordet',views.get_vendordet,name='get_vendordet'),
    path('get_customerdet',views.get_customerdet,name='get_customerdet'),
    path('recurbills_vendor',views.recurbills_vendor,name='recurbills_vendor'),
    path('vendor_dropdown',views.vendor_dropdown,name = 'vendor_dropdown'),
    path('recurbills_pay',views.recurbills_pay,name='recurbills_pay'),
    path('pay_dropdown',views.pay_dropdown,name = 'pay_dropdown'),
    path('recurbills_unit',views.recurbills_unit,name='recurbills_unit'),
    path('unit_dropdown',views.unit_dropdown,name = 'unit_dropdown'),
    path('recurbills_item',views.recurbills_item,name='recurbills_item'),
    path('item_dropdown',views.item_dropdown ,name = 'item_dropdown'),
    path('recurbills_account',views.recurbills_account,name='recurbills_account'),
    path('account_dropdown',views.account_dropdown ,name = 'account_dropdown'),
    path('get_rate',views.get_rate ,name = 'get_rate'),
    path('get_cust_state',views.get_cust_state,name = "get_cust_state"),
    path('export_pdf/<id>',views.export_pdf,name = "export_pdf"),
    path('recurbill_comment',views.recurbill_comment,name = "recurbill_comment"),
    path('recurbill_add_file/<id>',views.recurbill_add_file,name = "recurbill_add_file"),
    path('recurbill_email/<id>', views.recurbill_email, name='recurbill_email'),
    path('get_comments/<str:profile_name>/', views.get_comments, name='get_comments'),
    path('every_terms',views.every_terms,name='every_terms'),
    
    path('cust_create',views.cust_create,name='cust_create'),
    path('customer_me',views.customer_me,name='customer_me'),
    
    path('recurbills_customer',views.recurbills_customer,name='recurbills_customer'),
    path('customer_dropdown',views.customer_dropdown,name = 'customer_dropdown'),
    
    path('payment_termA',views.payment_termA,name='payment_termA'),
    path('entr_custmrA', views.entr_custmrA, name='entr_custmrA'),
    
    path('dashboard',views.dashboard, name='dashboard'),
    
    path('view_customr', views.view_customr, name='view_customr'),
    path('view_one_customer/<int:id>', views.view_one_customer, name='view_one_customer'),
    path('view_customr_sname', views.view_customr_sname, name='view_customr_sname'),
    path('view_customr_scpname', views.view_customr_scpname, name='view_customr_scpname'),
   
    path('editcustomer/<int:id>', views.editcustomer, name='editcustomer'),
    path('editEnter_customer/<int:id>', views.editEnter_customer, name='editEnter_customer'),
    path('delete_customr/<int:id>', views.delete_customr, name='delete_customr'),
    path('add_email_customer', views.add_email_customer, name='add_email_customer'),
    path('sendmail', views.sendmail, name='sendmail'),
    
    path('paymentmethod',views.paymentmethod,name='paymentmethod'),
    path('paymentadd_method',views.paymentadd_method,name='paymentadd_method'),
    path('payment_add_details',views.payment_add_details,name='payment_add_details'),
    
    path('payment_edit/<int:pk>',views.payment_edit,name='payment_edit'),
    path('payment_edit_view/<int:pk>',views.payment_edit_view,name='payment_edit_view'),
    
    path('purchaseView',views.purchaseView,name='purchaseView'),
  
    path('purchase_order',views.purchase_order,name='purchase_order'),
    path('purchase_vendor',views.purchase_vendor,name='purchase_vendor'),
    path('purchase_customer',views.purchase_customer,name='purchase_customer'),
    path('customer_dropdown',views.customer_dropdown,name='customer_dropdown'),
    path('payment_dropdown',views.payment_dropdown,name='payment_dropdown'),
    path('purchase_pay',views.purchase_pay,name='purchase_pay'),
    path('customer_det',views.customer_det,name='customer_det'),
    
    path('vendor_det',views.vendor_det,name='vendor_det'),
    path('create_Purchase_order',views.create_Purchase_order,name='create_Purchase_order'),
    path('purchase_unit',views.purchase_unit,name='purchase_unit'),
    path('purchase_unit_dropdown',views.purchase_unit_dropdown,name='purchase_unit_dropdown'),

    path('purchase_item',views.purchase_item,name='purchase_item'),
    path('purchase_item_dropdown',views.purchase_item_dropdown,name='purchase_item_dropdown'),

    path('purchase_account',views.purchase_account,name='purchase_account'),
    path('purchase_account_dropdown',views.purchase_account_dropdown,name='purchase_account_dropdown'),
    path('purchase_delet/<int:id>',views.purchase_delet,name='purchase_delet'),
    path('purchase_bill_view/<int:id>',views.purchase_bill_view,name='purchase_bill_view'),

    path('EmailAttachementView_purchase', views.EmailAttachementView_purchase, name='EmailAttachementView_purchase'),
    path('export_purchase_pdf/<id>',views.export_purchase_pdf,name = "export_purchase_pdf"),
    
    path('edit/<int:pk>',views.edit,name='edit'),
    path('change_status/<int:pk>',views.change_status,name='change_status'),
    path('change_status_draft/<int:pk>',views.change_status_draft,name='change_status_draft'),
    path('draft/<int:id>',views.draft,name='draft'),
    path('Approved/<int:id>',views.Approved,name='Approved'),


    path('edit_Purchase_order/<int:id>',views.edit_Purchase_order,name='edit_Purchase_order'),
    
    # Chart Of account


    path('chartofaccount_home',views.chartofaccount_home,name='chartofaccount_home'),
    path('create_account',views.create_account,name='create_account'),
    path('chartofaccount_view/<int:id>',views.chartofaccount_view,name='chartofaccount_view'),
    path('create_account_view',views.create_account_view,name='create_account_view'),
    path('edit_chart_of_account/<int:pk>',views.edit_chart_of_account,name="edit_chart_of_account"),
    path('upload_chart_of_account/<int:pk>',views.upload_chart_of_account,name="upload_chart_of_account"),
    path('download_chart_of_account/<int:pk>',views.download_chart_of_account,name="download_chart_of_account"),
    
    path('proj', views.proj, name='proj'),
	path('vproj', views.vproj, name='vproj'),
	path('addproj', views.addproj, name='addproj'),
	path('overview/<int:id>/', views.overview, name='overview'),
	path('editproj/<int:id>',views.editproj,name='editproj'),
	path('editprojdb/<int:id>',views.editprojdb,name='editprojdb'),
	path('delproj/<int:id>',views.delproj,name='delproj'),
	path('createuser', views.createuser, name='createuser'),
# 	path('comment/<int:id>', views.comment, name='comment'),
	path('commentdb/<int:pk>/', views.commentdb, name='commentdb'),
	path('toggle-status/<int:project_id>/', views.toggle_status, name='toggle_status'),
	path('itemdata2',views.itemdata2,name='itemdata2'),
	
	
	path("drf",views.drf,name='drf'),
    path('apr',views.apr,name='apr'),
    
    path('add_customers',views.add_customers,name='add_customers'),
    path('profileasc',views.profileasc,name='profileasc'),
    path('profiledesc',views.profiledesc,name='profiledesc'),
    
    path('paymentmade_reports',views.paymentmade_reports,name='paymentmade_reports'),
    path('get_account_number/',views.get_account_number,name='get_account_number'),
    path('payment_details_view/<int:payment_id>/', views.payment_details_view, name='payment_details_view'),
    path('payment_edit',views.payment_edit,name='payment_edit'),
    path('payment_lists/<int:payment_id>/', views.payment_lists, name='payment_lists'), 
    path('payment_template/<int:payment_id>/',views.payment_template,name='payment_template'),  
    path('payment/delete/<int:payment_id>',views.delete_payment,name='delete_payment'),
    path('payment_delete_details',views.payment_delete_details,name='payment_delete_details'),
    path('payment_details/<int:payment_id>/', views.payment_details, name='payment_details'),
	
	path('save-data/', views.save_data, name='save_data'),
	path('add_comment/<int:expense_id>/', views.add_comment, name='add_comment'),
	path('add_option',views.add_option,name='add_option'),
	path('options',views.options,name='options'),
    path('add_options',views.add_options,name='add_options'),
    path('marks',views.marks,name='marks'),
    path('payment_banking',views.payment_banking,name='payment_banking'),
    path('added_banking',views.added_banking,name='added_banking'),
    path('payment_banking_edit',views.payment_banking_edit,name='payment_banking_edit'),
    path('added_banking_edit',views.added_banking_edit,name='added_banking_edit'),
    path('delete_comment/<int:product_id>/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('save_bank_payment',views.save_bank_payment,name='save_bank_payment'),
    path('option_dropdown',views.option_dropdown,name='option_dropdown'),
    path('banking_dropdown',views.banking_dropdown,name='banking_dropdown'),
    
    path('payroll_create',views.payroll_create,name='payroll_create'),
    path('payroll_list',views.payroll_list,name='payroll_list'),
    path('createpayroll',views.createpayroll,name='createpayroll'),
    path('payroll_delete/<int:pid>',views.payroll_delete,name='payroll_delete'),
    path('payroll_view/<int:id>',views.payroll_view,name='payroll_view'),
    path('payroll_active/<int:id>',views.payroll_active,name='payroll_active'),
    path('payroll_file/<int:id>',views.payroll_file,name='payroll_file'),
    path('img_download/<int:id>',views.img_download,name='img_download'),
    path('file_download/<int:aid>',views.file_download,name='file_download'),
    path('payroll_edit/<int:pid>',views.payroll_edit,name='payroll_edit'),
    path('editpayroll/<int:id>',views.editpayroll,name='editpayroll'),
    path('add_payrollcomment/<int:pid>',views.add_payrollcomment,name='add_payrollcomment'),
    path('delete_payrollcomment/<int:cid>',views.delete_payrollcomment,name='delete_payrollcomment'),
    
    path('entr_custmrA1', views.entr_custmrA1, name='entr_custmrA1'),
    path('payment_termA1',views.payment_termA1,name='payment_termA1'),
    path('add_customers1',views.add_customers1,name='add_customers1'),
    path('projcomment/<int:id>', views.projcomment, name='projcomment'),
    path('projcommentdb/<int:id>', views.projcommentdb, name='projcommentdb'),
    
    path('expensepage',views.expensepage,name='expensepage'),
    path('save_expense',views.save_expense,name='save_expense'),
    path('add_accountE',views.add_accountE,name='add_accountE'),
    path('add_custmr',views.add_custmr,name='add_custmr'),
    # path('payment_terme',views.payment_terme,name='payment_terme'),
    # path('pay_dropdowne',views.pay_dropdowne,name = 'pay_dropdowne'),
    path('expense_details/<int:pk>',views.expense_details,name='expense_details'),
    path('edit_expensee/<int:expense_id>',views.edit_expensee,name='edit_expensee'),
    path('add_custmr/', views.add_custmr, name='add_custmr'),
    path('add_vendore/', views.add_vendore, name='add_vendore'),
    path('add_vendore', views.add_vendore, name='add_vendore'),
    path('delet/<int:id>',views.delet,name='delet'),
    # path('attach/<int:expense_id>',views.attach,name='attach'),
    path('upload_documents/<int:expense_id>',views.upload_documents,name='upload_documents'),
    path('account_dropdownE', views.account_dropdownE, name='account_dropdownE'),
    path('vendor_dropdownE/', views.vendor_dropdownE, name='vendor_dropdownE'),
    path('customer_dropdownE/', views.customer_dropdownE, name='customer_dropdownE'),
    path('save_expense/', views.save_expense, name='save_expense'),
    path('deletefile/<int:aid>',views.deletefile,name='deletefile'),
    
    path('recurbills_payzzz',views.recurbills_payzzz,name='recurbills_payzzz'),
    path('project_customer',views.project_customer,name='project_customer'),
    path('customer_dropdown_proj',views.customer_dropdown_proj,name='customer_dropdown_proj'),
    path('filter_by_draft',views.filter_by_draft,name='filter_by_draft'),
    path('filter_by_sent',views.filter_by_sent,name='filter_by_sent'),
    path('filter_by_draft_estimate_view/<int:pk>',views.filter_by_draft_estimate_view,name='filter_by_draft_estimate_view'),
    path('filter_by_sent_estimate_view/<int:pk>',views.filter_by_sent_estimate_view,name='filter_by_sent_estimate_view'),
    path('add_est_comment/<int:pk>',views.add_est_comment,name='add_est_comment'),
    
    path('report',views.report_view,name='report'),
    path('inventory_summary',views.inventory_summary,name='inventory_summary'),
    path('custom_repot',views.custom_repot,name='custom_repot'),
    path('inventory_Valuation_summary',views.inventory_Valuation_summary,name='inventory_Valuation_summary'),
    path('custom_valuation_repot',views.custom_valuation_repot,name='custom_valuation_repot'),
    path('show_hide',views.show_hide,name='show_hide'),
    path('general',views.general,name='general'),
    #Abin - Vendor Credits
    path('create_vendor_credit',views.create_vendor_credit,name='create_vendor_credit'),
    path('vendor_credits_home',views.vendor_credits_home,name='vendor_credits_home'), 
    path('vendor_credits',views.vendor_credits,name='vendor_credits'),
    path('getitems2',views.getitems2,name='getitems2'),
    path('show_credits/<int:pk>/', views.show_credits, name='show_credits'),
    path('delete_comment_credit/<int:pk>/<int:vid>', views.delete_comment_credit, name='delete_comment_credit'),
    path('credit_sendmail/<int:pk>',views.credit_sendmail,name='credit_sendmail'),
    path('edit_vendor_credits/<int:id>',views.edit_vendor_credits,name='edit_vendor_credits'),
    path('credit_upload_document/<int:pk>',views.credit_upload_document,name='credit_upload_document'),
    path('credit_download_doc/<int:pk>',views.credit_download_doc,name='credit_download_doc'),
    path('credit_delete_vendor/<int:pk>',views.credit_delete_vendor,name='credit_delete_vendor'),
    path('credits_statement/<int:id>',views.credits_statement,name='credits_statement'),
    path('additem_vendor_page',views.additem_vendor_page,name='additem_vendor_page'),
    path('add_customer_for_vcredit',views.add_customer_for_vcredit,name='add_customer_for_vcredit'),
    path('poject_itemz', views.poject_itemz, name='poject_itemz'),
    path('report_page', views.report, name='report_page'),
    path('fifo_cost', views.fifo_cost, name='fifo_cost'),
    path('product_sales_report', views.product_sales, name='product_sales_report'),
    path('product_customize', views.product_customize, name='product_customize'),
    path('customize_fifo', views.customize_fifo, name='customize_fifo'),
    path('add_vendor_credits',views.add_vendor_credits,name='add_vendor_credits'),
    path('get_vendor_credit_det',views.get_vendor_credit_det,name='get_vendor_credit_det'),
    path('get_vendor_credit_det1',views.get_vendor_credit_det1,name='get_vendor_credit_det1'),
    path('vendor_credit_vendor',views.vendor_credit_vendor,name='vendor_credit_vendor'),
    path('vendor_credit_dropdown',views.vendor_credit_dropdown,name = 'vendor_credit_dropdown'), 
    path('itemdata_vendor_credit',views.itemdata_vendor_credit,name='itemdata_vendor_credit'),
    path('vendor_credit_item',views.vendor_credit_item,name='vendor_credit_item'),
    path('vendor_credit_item_dropdown',views.vendor_credit_item_dropdown ,name = 'vendor_credit_item_dropdown'),
    path('view_vendor_credits/<id>',views.view_vendor_credits,name='view_vendor_credits'),   
    path('vendor_credit_comment',views.vendor_credit_comment,name = "vendor_credit_comment"),
    path('vendor_credit_add_file/<id>',views.vendor_credit_add_file,name = "vendor_credit_add_file"),
    path('vendor_credit_email/<id>', views.vendor_credit_email, name='vendor_credit_email'),  
    path('vc_view_vendorasc/<id>',views.vc_view_vendorasc,name='vc_view_vendorasc'),
    path('vc_view_vendordesc/<id>',views.vc_view_vendordesc,name='vc_view_vendordesc'), 
    path('delete_vendor_credits/<id>',views.delete_vendor_credits,name='delete_vendor_credits'),
    path('edit_vendor_credits/<int:pk>',views.edit_vendor_credits,name='edit_vendor_credits'),
    path('change_vendor_credits/<int:id>',views.change_vendor_credits,name='change_vendor_credits'),

    
    path('url1', views.product_customize, name='url1'),
    path('url2', views.show_customize_product, name='url2'),
    #------------------------------------------------------------------------------------------------sumayya---purchase bills
    path('view_bills',views.view_bills,name='view_bills'),
    path('new_bill/',views.new_bill,name='new_bill'),
    path('get_customer_data_bill/',views.get_customer_data_bill,name='get_customer_data_bill'),
    path('get_vendor_data_bill/',views.get_vendor_data_bill,name='get_vendor_data_bill'),
    path('create_purchase_bill/',views.create_purchase_bill,name='create_purchase_bill'),
    path('create_purchase_bill1/',views.create_purchase_bill1,name='create_purchase_bill1'),
    path('itemdata_bills/',views.itemdata_bills,name='itemdata_bills'),
    path('bill_view/<int:b_id>',views.bill_view,name='bill_view'),
    path('edit_bill/<int:bill_id>',views.edit_bill,name='edit_bill'),
    path('update_bills/<int:pk>',views.update_bills,name='update_bills'),
    path('add_comment_bills/<int:bill_id>',views.add_comment_bills,name='add_comment_bills'),
    path('upload_file_bills/<int:bill_id>',views.upload_file_bills,name='upload_file_bills'),
    path('delete_bill/<int:bill_id>',views.delete_bill,name='delete_bill'),
    path('search_bill/',views.search_bill,name='search_bill'),
    path('entr_custmr_for_bills/',views.entr_custmr_for_bills,name='entr_custmr_for_bills'),
    path('add_vendor_bills/',views.add_vendor_bills,name='add_vendor_bills'),
    path('additem_bills/',views.additem_bills,name='additem_bills'),
    path('create_account_bills/',views.create_account_bills,name='create_account_bills'),
    path('create_payment_terms_bills/',views.create_payment_terms_bills,name='create_payment_terms_bills'),
    
    path('expense_pay', views.expense_pay, name='expense_pay'),
    path('pay_dropdownE', views.pay_dropdownE, name='pay_dropdownE'),
    path('get_vendor_gst_treatment', views.get_vendor_gst_treatment, name='get_vendor_gst_treatment'),
    path('get_company_state', views.get_company_state, name='get_company_state'),
    
    path('report_inventory_view',views.report_inventory_view,name='report_inventory_view'),
    path('reports',views.reports,name='reports'),
    path('salesby_customer',views.salesby_customer,name='salesby_customer'),
    path('customize_report/', views.customize_report, name='customize_report'),
    path('general_customize', views.general_customize, name='general_customize'),
    path('salesby_item',views.salesby_item,name='salesby_item'),
    path('customize_report1/', views.customize_report1, name='customize_report1'),
    
    path('customerAtoZ_bills',views.customerAtoZ_bills,name='customerAtoZ_bills'),
    path('vendorAtoZ_bills',views.vendorAtoZ_bills,name='vendorAtoZ_bills'),
    path('add_email_customer/<int:id>', views.add_email_customer, name='add_email_customer'),
    path('sendmails/<int:id>', views.sendmails, name='sendmails'),
    path('cust_comments/<int:id>', views.cust_comments, name='cust_comments'),
    path('cust_Attach_files/<int:id>', views.cust_Attach_files, name='cust_Attach_files'),
    
    path('sales_order', views.sales_order, name='sales_order'),
    path('sales_summery', views.sales_summery, name='sales_summery'),
    path('transaction/<int:pk>', views.transaction, name="transaction"),
    
    path('view_sales_order_all',views.view_sales_order_all,name='view_sales_order_all'),
    path('view_sales_order_Draft',views.view_sales_order_Draft,name='view_sales_order_Draft'),
    path('view_sales_order_approved',views.view_sales_order_approved,name='view_sales_order_approved'),
    path('customer_dropdown_sales',views.customer_dropdown_sales,name='customer_dropdown_sales'),
    
    path('gstr2_load',views.gstr2_load,name='gstr2_load'),
    path('sales_by_hsn_load',views.sales_by_hsn_load,name="sales_by_hsn_load"),
    path('export_sales_pdf/<int:id>',views.export_sales_pdf,name='export_sales_pdf'),
    
    #--------------------------shamreena---GSTR1 & GSTR_3B
  
    path('GSTR_3Bpage',views.GSTR_3Bpage,name='GSTR_3Bpage'),
    path('GSTR_1page',views.GSTR_1page,name='GSTR_1page'),
    
    path('change_vendor_status/<int:pk>', views.change_vendor_status, name='change_vendor_status'),
    
    #reshna-banking    
    path('bank_home', views.bank_home, name='bank_home'),
    path('create_bank', views.create_bank, name='create_bank'),
    path('edit_bank/<int:bank_id>', views.edit_bank, name='edit_bank'),
    path('bank_listout/<int:id>', views.bank_listout, name='bank_listout'),
    path('banktocash/<int:id>', views.banktocash, name='banktocash'),
    path('bank_attachfile/<int:id>', views.bank_attachfile, name='bank_attachfile'),
    path('delete_bank/<int:bank_id>', views.delete_bank, name='delete_bank'),
    path('nameasc/', views.nameasc, name='nameasc'),
    path('namedes/', views.namedes, name='namedes'),
    path('view_nameasc/<int:id>/', views.view_nameasc, name='view_nameasc'),
    path('view_namedes/<int:id>/', views.view_namedes, name='view_namedes'),
    path('bank_pdf/<int:id>/', views.bank_pdf, name='bank_pdf'),
    path('bank_status/<int:id>/', views.bank_status, name='bank_status'),
    
    path('load_balance_sheet/',views.load_balance_sheet,name='load_balance_sheet'),
    path('load_horizontal_balance_sheet/',views.load_horizontal_balance_sheet,name='load_horizontal_balance_sheet'),
    path('load_customize_report_bs/',views.load_customize_report_bs,name='load_customize_report_bs'),
    path('load_customize_report_hbs/',views.load_customize_report_hbs,name='load_customize_report_hbs'),
    
    path('vendor_credits_pay',views.vendor_credits_pay,name = 'vendor_credits_pay'),
    path('vendor_credits_pay_dropdown',views.vendor_credits_pay_dropdown,name = 'vendor_credits_pay_dropdown'),
    path('vendor_credits_unit',views.vendor_credits_unit,name = 'vendor_credits_unit'),
    path('vendor_credits_unit_dropdown',views.vendor_credits_unit_dropdown,name = 'vendor_credits_unit_dropdown'),
    path('vendor_credits_account',views.vendor_credits_account,name='vendor_credits_account'),
    path('vendor_credits_account_dropdown',views.vendor_credits_account_dropdown,name='vendor_credits_account_dropdown'),
    path('export_vendor_credit_pdf/<id>',views.export_vendor_credit_pdf,name = "export_vendor_credit_pdf"),
    
    path('party_statement',views.party_statement,name='party_statement'),
    path('get_transactions',views.get_transactions,name='get_transactions'),
    path('all_parties',views.all_parties,name='all_parties'),
    path('update_balancesheet/',views.update_balancesheet,name='update_balancesheet'),
    path('update_hbalancesheet/',views.update_hbalancesheet,name='update_hbalancesheet'),
    
    path('purchasebyvendor',views.purchasebyvendor,name='purchasebyvendor'),
    path('customize_vendor_report',views.customize_vendor_report,name='customize_vendor_report'),
    path('purchasebyitem',views.purchasebyitem,name='purchasebyitem'),
    path('customize_report_purchasebyitem',views.customize_report_purchasebyitem,name='customize_report_purchasebyitem'),
    
    path('ewaylistout',views.ewaylistout,name='ewaylistout'),
    path('ewaycreate',views.ewaycreate,name='ewaycreate'),
    path('recurbills_pay_eway',views.recurbills_pay_eway,name='recurbills_pay_eway'),
    path('ewayb_customer',views.ewayb_customer,name='ewayb_customer'),
    path('customer_dropdown_ewayb',views.customer_dropdown_ewayb,name='customer_dropdown_ewayb'),
    path('add-transportation/', views.add_transportation, name='add_transportation'),
    path('ewaybills_item',views.ewaybills_item,name='ewaybills_item'),
    path('eway_item_dropdown',views.eway_item_dropdown ,name = 'eway_item_dropdown'),
    path('eway_unit',views.eway_unit,name='eway_unit'),
    path('eway_unit_dropdown',views.eway_unit_dropdown,name = 'eway_unit_dropdown'),
    path('unit_get_rate',views.unit_get_rate ,name = 'unit_get_rate'),
    path('create_ewaybillz',views.create_ewaybillz,name='create_ewaybillz'),
    path('ewayoverview/<int:id>/',views.ewayoverview,name='ewayoverview'),
    path('delete_ewaybills/<id>',views.delete_ewaybills,name='delete_ewaybills'),
    path('ewayedit/<int:id>/',views.ewayedit,name='ewayedit'),
    path('ewaybill_comment',views.ewaybill_comment,name = "ewaybill_comment"),
    path('ewayeditdb/<int:id>/',views.ewayeditdb,name='ewayeditdb'),
    path('ewaycommentdb/<int:id>', views.ewaycommentdb, name='ewaycommentdb'),
    path('get-transportation-options/', views.get_transportation_options, name='get_transportation_options'),
    
    path('filter_invoice_draft',views.filter_invoice_draft,name='filter_invoice_draft'),
    path('filter_invoice_sent',views.filter_invoice_sent,name='filter_invoice_sent'),
    path('add_invoice_comment/<int:pk>',views.add_invoice_comment,name='add_invoice_comment'),
    path('filter_inv_det_draft/<int:id>',views.filter_inv_det_draft,name='filter_inv_det_draft'),
    path('filter_inv_det_send/<int:id>',views.filter_inv_det_send,name='filter_inv_det_send'),
    
    path('filter_retainer_draft',views.filter_retainer_draft,name='filter_retainer_draft'),
    path('filter_retainer_sent',views.filter_retainer_sent,name='filter_retainer_sent'),
    path('filter_retainer_view_sent/<int:pk>',views.filter_retainer_view_sent,name='filter_retainer_view_sent'),
    path('filter_retainer_view_draft/<int:pk>',views.filter_retainer_view_draft,name='filter_retainer_view_draft'),
    path('add_ret_invoice_comment/<int:pk>',views.add_ret_invoice_comment,name='add_ret_invoice_comment'),
    
    path('filter_delivery_draft',views.filter_delivery_draft,name="filter_delivery_draft"),
    path('filter_delivery_sent',views.filter_delivery_sent,name="filter_delivery_sent"),
    path('filter_by_draft_chellan_view/<int:pk>',views.filter_by_draft_chellan_view,name='filter_by_draft_chellan_view'),
    path('filter_by_sent_chellan_view/<int:pk>',views.filter_by_sent_chellan_view,name='filter_by_sent_chellan_view'),
    path('add_delivery_chellan_comment/<int:pk>',views.add_delivery_chellan_comment,name='add_delivery_chellan_comment'),
    
    path('purchase_customer_eway',views.purchase_customer_eway,name='purchase_customer_eway'),
    path('get_vendor_list',views.get_vendor_list,name='get_vendor_list'),
    path('get_vendor_data',views.get_vendor_data,name='get_vendor_data'),
    path('expense_comment/<int:expense_id>/', views.expense_comment, name='expense_comment'),
    path('delete_expense_comment/<int:expense_id>/<int:comment_id>/', views.delete_expense_comment, name='delete_expense_comment'),
    path('get_customer_email',views.get_customer_email,name='get_customer_email'),
    path('toggle_expense_status/<int:expense_id>',views.toggle_expense_status,name='toggle_expense_status'),
    path('custmr_payment',views.custmr_payment,name='custmr_payment'),
    path('get_vendor_gst/<int:vendor_id>',views.get_vendor_gst, name='get_vendor_gst'),
    
    path('creditnotes',views.creditnotes,name='creditnotes'),
    path('newcredit',views.newcredit,name='newcredit'),
    path('creditnote_view/<int:creditnote_id>/', views.creditnote_view, name='creditnote_view'),
    path('add_creditnotes/',views.add_creditnotes ,name='add_creditnotes'), #updated
    path('load_initial_items/', views.load_initial_items, name='load_initial_items'),
    path('credit_template',views.credit_template,name='credit_template'),
    path(' purchase_item_dropdown1',views. purchase_item_dropdown1,name='purchase_item_dropdown1'),
    path('file_download1',views.file_download1,name='file_download1'),
    path('deletefile1',views.deletefile1,name='deletefile1'),
    path('editdb/<int:pk>', views.editdb, name='editdb'),
    path('edit_creditnote/<int:pk>', views.edit_creditnote, name='edit_creditnote'),
    path('fetch_customers_from_creditnotes/', views.fetch_customers_from_creditnotes, name='fetch_customers_from_creditnotes'),
    path('delete_creditnote/<int:pk>/', views.delete_creditnote, name='delete_creditnote'),
    path('add_comment_creditnotes/<int:creditnote_id>',views.add_comment_creditnotes,name='add_comment_creditnotes'),
    path('creditnote_add_file/<int:pk>',views.creditnote_add_file,name = "creditnote_add_file"),
    
    path('customer_balances',views.customer_balances,name="customer_balances"),
    path('delivery_challan',views.delivery_challan,name="delivery_challan"),
    path('show_customize_challan',views.show_customize_challan,name="show_customize_challan"),
    path('url4', views.challan_customize, name='url4'),
    path('url3', views.show_customize_challan, name='url3'),
    path('custom_report',views.custom_report,name="custom_report"),
    path('challan_customize',views.challan_customize,name="challan_customize"),
    
    #Athul
    
    path('sort_product_name/<int:id>', views.sort_product_name, name='sort_product_name'),
    path('sort_product_hsn/<int:id>', views.sort_product_hsn, name='sort_product_hsn'),
    path('commentproduct/<int:product_id>', views.commentproduct, name='commentproduct'),
    path('salesgraph/<str:product>', views.salesgraph, name='salesgraph'),
    path('salesby_item_filter', views.salesby_item_filter, name='salesby_item_filter'),
    path('salesby_item_graph_filter/<str:product>', views.salesby_item_graph_filter, name='salesby_item_graph_filter'),
    
    path('create_loan/', views.create_loan, name='create_loan'),
    path('employee/list/', views.employee_list, name='employee_list'),
    path('delete_loan/<int:loan_id>/', views.delete_loan, name='delete_loan'),

    path('edit_loan/<int:loan_id>/', views.edit_loan, name='edit_loan'),
     
    path('employee/<int:payroll_id>/loan/', views.employee_loan_details, name='employee_loan_details'),
    path('edit_loan/<int:loan_id>/', views.edit_loan, name='edit_loan'),
    path('loan/activate/<int:loan_id>/', views.activate_loan, name='activate_loan'),
    path('loan/deactivate/<int:loan_id>/', views.deactivate_loan, name='deactivate_loan'),
    path('toggle_loan_active/<int:loan_id>/', views.toggle_loan_active, name='toggle_loan_active'),

    path('employee_loan_template/<int:payroll_id>/', views.employee_loan_template, name='employee_loan_template'),

    path('add_loan_comment/<int:payroll_id>/', views.add_loan_comment, name='add_loan_comment'),
    path('delete_loan_comment/<int:comment_id>/', views.delete_loan_comment, name='delete_loan_comment'),

    path('add_loan_attach/<int:payroll_id>/', views.add_loan_attach, name='add_loan_attach'),

    path('download_loan_attach/<int:payroll_id>/<int:attachment_id>/', views.download_loan_attach, name='download_loan_attach'),
    path('delete_loan_attach/<int:attach_id>/', views.delete_loan_attach, name='delete_loan_attach'),


    path('loan_active/<int:loan_id>',views.loan_active,name='loan_active'),
    path('loan_deactive/<int:loan_id>',views.loan_deactive,name='loan_deactive'),

    path('add_loan_comment_template/<int:payroll_id>/', views.add_loan_comment_template, name='add_loan_comment_template'),
    path('delete_loan_comment_template/<int:comment_id>/', views.delete_loan_comment_template, name='delete_loan_comment_template'),
    path('delete_loan_attach_template/<int:attach_id>/', views.delete_loan_attach_template, name='delete_loan_attach_template'),
    path('add_loan_attach_template/<int:payroll_id>/', views.add_loan_attach_template, name='add_loan_attach_template'),
    path('createpayroll2',views.createpayroll2,name='createpayroll2'),
    path('loan_dropdown',views.loan_dropdown,name = 'loan_dropdown'),
    path('loan_dropwithoutreload/<int:employee_id>/', views.loan_dropwithoutreload, name='loan_dropwithoutreload'),
    # Rijin- end of urls (employee_loan)
    
    path('get_customerdet_eway',views.get_customerdet_eway,name='get_customerdet_eway'),
    path('purchase_item_eway',views.purchase_item_eway,name='purchase_item_eway'),
    path('purchase_item_dropdown_eway',views.purchase_item_dropdown_eway,name='purchase_item_dropdown_eway'),
    path('purchase_unit_eway',views.purchase_unit_eway,name='purchase_unit_eway'),
    path('purchase_unit_dropdown_eway',views.purchase_unit_dropdown_eway,name='purchase_unit_dropdown_eway'),
    
    path('vendorbal_cus',views.vendorbal_customer,name='vendorbal_cus'),
    path('bill_details',views.bill_details,name='bill_details'),
    path('vendor_customize_report',views.vendor_customize_report,name='vendor_customize_report'),
    path('bill_customize_report',views.bill_customize_report,name='bill_customize_report'),
    
    path('daybook',views.daybook,name='daybook'),
    path('creditnote_details',views.creditnote_details,name='creditnote_details'),
    
    path('add_recurring_vendor/',views.add_recurring_vendor,name='add_recurring_vendor'),
    path('payment_view',views.payment_view,name='payment_view'),
    path('get_customer_namess', views.get_customer_namess, name='get_customer_namess'),
    path('save_recurring_data/', views.save_recurring_data, name='save_recurring_data'),
    path('entr_recurring_custmr',views.entr_recurring_custmr,name='entr_recurring_custmr'),
    path('get_repeat_every',views.get_repeat_every,name='get_repeat_every'),
    
    #...................................mirna.........manual journal..............

    path('manual_journal_home/',views.manual_journal_home, name='manual_journal_home'),
    path('add_journal/',views.add_journal, name='add_journal'),
    path('journal_list/', views.journal_list, name='journal_list'),
    path('get_journal_details/<int:journal_id>/', views.get_journal_details, name='get_journal_details'),
    path('get_journal_details_for_overview/<int:journal_id>/', views.get_journal_details_for_overview, name='get_journal_details_for_overview'),
    path('update_journal_status/<int:journal_id>/', views.update_journal_status, name='update_journal_status'),
    path('get_journal_comments/<int:journal_id>/', views.get_journal_comments, name='get_journal_comments'),
    path('save_journal_comment/<int:journal_id>/', views.save_journal_comment, name='save_journal_comment'),
    path('delete_journal_comment/<int:comment_id>/', views.delete_journal_comment, name='delete_journal_comment'),
    path('edit_journal/<int:journal_id>/', views.edit_journal, name='edit_journal'),
    path('delete_journal/<int:journal_id>/', views.delete_journal, name='delete_journal'),
    path('get_journal_attachment/<int:journal_id>/', views.get_journal_attachment, name='get_journal_attachment'),
    path('save_pdf/', views.save_pdf, name='save_pdf'),
    path('create_account_jrnl/', views.create_account_jrnl, name='create_account_jrnl'),
    path('journal_account_dropdown',views.journal_account_dropdown ,name = 'journal_account_dropdown'),
    
    #------------------------shamreena---inventory details---
    path('inven_details',views.inven_details,name='inven_details'),
    path('invengraph/<str:product>',views.invengraph,name='invengraph'),
    path('invenitem_graph_filter/<str:product>', views.invenitem_graph_filter, name='invenitem_graph_filter'),
    path('inventorysalegraph',views.inventorysalegraph,name='inventorysalegraph'),
    #--End---
    
    path('update_creditnote_status/<int:creditnote_id>/', views.update_creditnote_status, name='update_creditnote_status'),
    path('credit_customer',views.credit_customer,name='credit_customer'),
    path('customer_dropdown_credit',views.customer_dropdown_credit,name='customer_dropdown_credit'),
    
    # new customer correction works..............................................................

    path('add_comment_cust/<int:id>',views.add_comment_cust,name='add_comment_cust'),
    path('amtcu',views.amtcus,name='amtcus'),
    path('payment_terms_cust',views.payment_terms_cust,name='payment_terms_cust'),
    path('delete_customer/<int:id>',views.delete_customer,name='delete_customer'),
    path('customer_active/<int:id>',views.customer_active,name='customer_active'),
    path('active_cust',views.active_cust,name='active_cust'),
    path('inactive_cust',views.inactive_cust,name='inactive_cust'),
    path('cust_sname/<int:id>',views.cust_sname,name='cust_sname'),
    path('cust_amt/<int:id>',views.cust_amt,name='cust_amt'),
    path('emailattachment_cust',views.emailattachment_cust,name='emailattachment_cust'),
    path('new_recur1',views.new_recur1,name='new_recur1'),
    path('add_comment_recur/<int:id>',views.add_comment_recur,name='add_comment_recur'),
    path('customerasc',views.customerasc,name='customerasc'),
    path('amtasc',views.amtasc,name='amtasc'),
    path('draft_to_save/<int:id>',views.draft_to_save,name='draft_to_save'),
    path('profilename',views.profilename,name='profilename'),
    path('recurname/<int:id>',views.recurname,name='recurname'),
    # path('recurcust',views.recurcust,name='recurcust'),
    path('recuramt/<int:id>',views.recuramt,name='recuramt'),
    # ....................................................................................................
    
    path('inventory_adjustment',views.inventory_adjustment,name='inventory_adjustment'),
    path('new_adjustment',views.new_adjustment,name='new_adjustment'),
    path('newreasons',views.newreasons,name='newreasons'),
    path('save_adjustment',views.save_adjustment,name='save_adjustment'),
    path('inv_overview/<int:id>/',views.inv_overview,name='inv_overview'),
    path('add_inv_comment/<int:id>/',views.add_inv_comment,name='add_inv_comment'),
    path('change_inventory_status/<int:id>/',views.change_inventory_status,name='change_inventory_status'),
    path('delete_inventory/<int:id>/',views.delete_inventory,name='delete_inventory'),
    path('filterby_draft/<int:id>/',views.filterby_draft,name='filterby_draft'),
    path('filterby_adjusted/<int:id>/',views.filterby_adjusted,name='filterby_adjusted'),
    path('edit_inventory/<int:id>/',views.edit_inventory,name='edit_inventory'),
    path('update_adjustment/<int:id>/',views.update_adjustment,name='update_adjustment'),
    path('newreasonslist',views.newreasonslist,name='newreasonslist'),
    
    #------------------------------reports-Profit and Loss & Profit and Loss (schedule lll)--------Merlin-----------------------
    
    path('profit_and_loss',views.profit_and_loss,name='profit_and_loss'),
    path('profit_and_loss_customize_report',views.profit_and_loss_customize_report,name='profit_and_loss_customize_report'),
    path('prft_and_ls_custmz_rprt_shw_hide',views.prft_and_ls_custmz_rprt_shw_hide,name='prft_and_ls_custmz_rprt_shw_hide'),
    path('profit_and_loss_schedule_III',views.profit_and_loss_schedule_III,name='profit_and_loss_schedule_III'),
    path('profit_and_loss_scedule_iii_customize_report',views.profit_and_loss_scedule_iii_customize_report,name='profit_and_loss_scedule_iii_customize_report'),
    
    
    path('recurinvoice_customer',views.recurinvoice_customer,name='recurinvoice_customer'),
    path('horizontal_profit_and_loss',views.horizontal_profit_and_loss,name='horizontal_profit_and_loss'),
    path('customize_report_hpl',views.customize_report_hpl,name='customize_report_hpl'),
    path('balance_sheet_sthree',views.balance_sheet_sthree,name='balance_sheet_sthree'),
    path('customize_report_bss3',views.customize_report_bss3,name='customize_report_bss3'),
    path('profit_and_loss_pdf',views.profit_and_loss_pdf,name='profit_and_loss_pdf'),
    path('profit_and_loss_schedule_III_pdf',views.profit_and_loss_schedule_III_pdf,name='profit_and_loss_schedule_III_pdf'),
    
    #---------vendor corrections----sumayya---------------------------------------------------------------
    path('view_vendor_active',views.view_vendor_active,name='view_vendor_active'),
    path('view_vendor_inactive',views.view_vendor_inactive,name='view_vendor_inactive'),
    path('sort_vendor_by_name',views.sort_vendor_by_name,name='sort_vendor_by_name'),
    path('sort_vendor_by_amount',views.sort_vendor_by_amount,name='sort_vendor_by_amount'),
    path('sort_vendor_by_name_det/<int:pk>',views.sort_vendor_by_name_det,name='sort_vendor_by_name_det'),
    path('sort_vendor_by_amount_det/<int:pk>',views.sort_vendor_by_amount_det,name='sort_vendor_by_amount_det'),


    #----------------------------------------------------------------------------------------------------
    
    path('new_item',views.new_item,name='new_item'),
    path('new_item_dropdown',views.new_item_dropdown,name='new_item_dropdown'),
    
    path('termdata',views.termdata,name='termdata'),
    path('bankdata',views.bankdata,name='bankdata'),
    path('convert_to_invoice/<int:pk>',views.convert_to_invoice,name='convert_to_invoice'),
    path('convert_view/<int:pk>',views.convert_view,name='convert_view'),
    
    path('holidays/<str:date>',views.holidays,name='holidays'),

    path('all_events/', views.all_events, name='all_events'), 
    path('add_holiday/', views.add_holiday, name='add_holiday'), 
    path('remove/<int:id>', views.remove, name='remove'),

    path('create_emp', views.create_emp, name='create_emp'),
    path('getemployee', views.getemployee, name='getemployee'),
    path('project_file/<int:id>', views.project_file, name='project_file'),
    path('add_projectcomment/<int:id>', views.add_projectcomment, name='add_projectcomment'),
    path('delete_projectcomment/<int:cid>', views.delete_projectcomment, name='delete_projectcomment'),
    path('project_summary', views.project_summary, name='project_summary'),

    path('projfile_download/<int:aid>', views.projfile_download, name='projfile_download'),
    path('projdeletefile/<int:aid>', views.projdeletefile, name='projdeletefile'),
    path('purchase_item_dropdown_credit/',views.purchase_item_dropdown_credit,name='purchase_item_dropdown_credit'),
    path('purchase_item_credit/', views.purchase_item_credit, name='purchase_item_credit'),
    path('purchase_unit_credit',views.purchase_unit_credit,name='purchase_unit_credit'),
    path('purchase_unit_dropdown_credit',views.purchase_unit_dropdown_credit,name='purchase_unit_dropdown_credit'),
    path('get_item_details/', views.get_item_details, name='get_item_details'),
    
    path('project_active/<int:id>', views.project_active, name='project_active'),
    path('holiday_list',views.holiday_list,name='holiday_list'),
    path('projentr_custmrA',views.projentr_custmrA,name='projentr_custmrA'),
    
    #-----------------------------Ashikh V U payment_received(start)-------------------------
    path('payment_received',views.payment_received,name='payment_received'),
    path('generate_pdf/<str:string_date>/<str:start_d>/<str:end_d>', views.generate_pdf, name='generate_pdf'),
    path('payment_reciedved_customize',views.payment_reciedved_customize,name='payment_reciedved_customize'),
    path('payment_reciedved_customize_sub/<str:new_id>',views.payment_reciedved_customize_sub,name='payment_reciedved_customize_sub'),
    path('select_comparator/<str:new_id>',views.select_comparator,name='select_comparator'),
    path('add_note_or_date/<str:selected_option>/<str:new_id>',views.add_note_or_date,name='add_note_or_date'),
    path('empty_filter',views.empty_filter,name='empty_filter'),
    path('payment_reciedved_customize_show',views.payment_reciedved_customize_show,name='payment_reciedved_customize_show'),
    path('my_calendar',views.my_calendar,name='my_calendar'),
    path('tax_summary_page',views.tax_summary_page,name='tax_summary_page'),
    path('generate_pdf1/<str:string_date>/<str:start_d>/<str:end_d>', views.generate_pdf1, name='generate_pdf1'),
    path('tax_summary_customize_general/', views.tax_summary_customize_general, name='tax_summary_customize_general'),
    path('set_custom_date', views.set_custom_date, name='set_custom_date'),
    #-----------------------------Ashikh V U payment_received(start)-------------------------
    
    path('hsndata',views.hsndata,name='hsndata'),
    
    path('delete_purchase_bill/<int:id>',views.delete_purchase_bill,name='delete_purchase_bill'),
    path('add_repeat',views.add_repeat,name='add_repeat'),
    path('repeat_dropdown',views.repeat_dropdown,name='repeat_dropdown'),
    path('get_rec_item',views.get_rec_item,name='get_rec_item'), 
    path('draft_recurring_bills',views.draft_recurring_bills,name='draft_recurring_bills'), 
    path('add_rec_comments/<int:id>', views.add_rec_comments, name='add_rec_comments'),
    path('delete_rec_comments/<int:id>/<int:commentid>', views.delete_rec_comments, name='delete_rec_comments'),
    path('change_draft_recurring_bills/<int:id>/',views.change_draft_recurring_bills,name='change_draft_recurring_bills'), 
    path('covert_to_recurring_bills/<int:id>/',views.covert_to_recurring_bills,name='covert_to_recurring_bills'),
    path('recur_bill_save/<int:id>',views.recur_bill_save,name='recur_bill_save'),
    path('recur_bill_draft/<int:id>',views.recur_bill_draft,name='recur_bill_draft'),
    path('billno_recurring_sort/<int:id>',views.billno_recurring_sort,name='billno_recurring_sort'),
    path('vendor_recurring_sort/<int:id>',views.vendor_recurring_sort,name='vendor_recurring_sort'),
    path('profilename_recurring_sort/<int:id>',views.profilename_recurring_sort,name='profilename_recurring_sort'),
    path('add_purchase_comments/<int:id>', views.add_purchase_comments, name='add_purchase_comments'),
    path('delete_purchase_comments/<int:id>/<int:commentid>', views.delete_purchase_comments, name='delete_purchase_comments'),
    path('covert_to_purchase_bills/<int:id>/',views.covert_to_purchase_bills,name='covert_to_purchase_bills'),
    path('update_bills_save/<int:pk>',views.update_bills_save,name='update_bills_save'),
    path('billno_purchase_sort/<int:b_id>',views.billno_purchase_sort,name='billno_purchase_sort'),
    path('vendor_purchase_sort/<int:b_id>',views.vendor_purchase_sort,name='vendor_purchase_sort'),
    path('customer_purchase_sort/<int:b_id>',views.customer_purchase_sort,name='customer_purchase_sort'),
    path('purchase_bill_save/<int:b_id>',views.purchase_bill_save,name='purchase_bill_save'),
    path('purchase_bill_draft/<int:b_id>',views.purchase_bill_draft,name='purchase_bill_draft'),
    
    path('terms_dropdowns',views.terms_dropdowns,name='terms_dropdowns'),
    
    #Nikhila
    path('new_estimate_customer',views.new_estimate_customer,name='new_estimate_customer'),
    path('new_estimate_item',views.new_estimate_item,name='new_estimate_item'),
    path('convert_to_salesorder/<int:pk>',views.convert_to_salesorder,name='convert_to_salesorder'),
    path('estimste_status_edit/<int:pk>',views.estimste_status_edit,name='estimste_status_edit'),
    path('est_sort_by_name',views.est_sort_by_name,name='est_sort_by_name'),
    path('est_sort_by_estno',views.est_sort_by_estno,name='est_sort_by_estno'),
    path('est_sort_by_name_estimate_view/<int:pk>',views.est_sort_by_name_estimate_view,name='est_sort_by_name_estimate_view'),
    path('est_sort_by_estno_estimate_view/<int:pk>',views.est_sort_by_estno_estimate_view,name='est_sort_by_estno_estimate_view'),

    path('retainer_invoice_sort_by_name',views.retainer_invoice_sort_by_name,name='retainer_invoice_sort_by_name'),
    path('retainer_invoice_sort_by_no',views.retainer_invoice_sort_by_no,name='retainer_invoice_sort_by_no'),
    path('sort_retainer_view_name/<int:pk>',views.sort_retainer_view_name,name='sort_retainer_view_name'),
    path('sort_retainer_view_no/<int:pk>',views.sort_retainer_view_no,name='sort_retainer_view_no'),
    path('ret_invoice_status_edit/<int:pk>',views.ret_invoice_status_edit,name='ret_invoice_status_edit'),
    path('get_retainer_accno',views.get_retainer_accno,name='get_retainer_accno'),

    path('go_settings',views.go_settings,name='go_settings'),
    path('edit_setting/<int:pk>',views.edit_setting,name='edit_setting'),
    #End
    
    path('item_statuschange/<int:id>',views.item_statuschange,name='item_statuschange'),
    
    # .........................................Godown(new)........................Antony Tom------------
    path('add_godown',views.add_godown,name='add_godown'),
    path('view_godown',views.view_godown,name='view_godown'),
    path('get_itemsdet',views.get_itemsdet,name='get_itemsdet'),
    path('get_item_info/<int:item_id>/', views.get_item_info, name='get_item_info'),
    path('save_godown',views.save_godown,name='save_godown'),
    path('add_modalgodown',views.add_modalgodown,name='add_modalgodown'),
    path('add_unitmodal',views.add_unitmodal,name='add_unitmodal'), 
    path('godownoverview/<int:id>',views.godownoverview,name='godownoverview'),
    path('godown_edit/<int:id>',views.godown_edit,name='godown_edit'),
    path('edit_savegodown/<int:id>',views.edit_savegodown,name='edit_savegodown'),
    path('deletegodownoverview/<int:id>',views.deletegodownoverview,name='deletegodownoverview'),
    path('commentgodown/<int:product_id>',views.commentgodown,name='commentgodown'),
    path('delete_commentgodown/<int:product_id>/<int:comment_id>/', views.delete_commentgodown, name='delete_commentgodown'),
    path('deleteviewgodown/<int:id>/', views.deleteviewgodown, name='deleteviewgodown'),
    path('godown_active/<int:id>', views.godown_active, name='godown_active'),
    path('upload_documentsgodown/<int:godown_id>',views.upload_documentsgodown,name='upload_documentsgodown'),
    path('editcommentgodown/<int:product_id>',views.editcommentgodown,name='editcommentgodown'),
    path('add_sales_godown',views.add_sales_godown,name='add_sales_godown'),
    path('godownmodal_unit',views.godownmodal_unit,name='godownmodal_unit'),
    path('godownunit_dropdown',views.godownunit_dropdown,name='godownunit_dropdown'),
    
    #End
    
    path('get_customer_gsttrmnt',views.get_customer_gsttrmnt,name='get_customer_gsttrmnt'),
    path('get_vendor_place_of_supply/', views.get_vendor_place_of_supply, name='get_vendor_place_of_supply'), 
    path('recurring_expense_details', views.recurring_expense_details, name='recurring_expense_details'), 
    path('recurring_expense_draft/<int:expense_id>', views.recurring_expense_draft, name='recurring_expense_draft'), 
    path('recurring_expense_save/<int:expense_id>', views.recurring_expense_save, name='recurring_expense_save'),
    path('draft_expense',views.draft_expense,name='draft_expense'),
    path('covert_to_status/<int:id>',views.covert_to_status,name='covert_to_status'),
    
    path('invoice_details',views.invoice_details,name='invoice_details'),
    
    path('payment_type_cash_in_hand',views.payment_type_cash_in_hand,name='payment_type_cash_in_hand'),
    path('generate_pdf3/<str:string_date>/<str:start_d>/<str:end_d>', views.generate_pdf3, name='generate_pdf3'),
    path('payment_type_upi',views.payment_type_upi,name='payment_type_upi'),
    path('generate_pdf4/<str:jsondict>/<str:start_d>/<str:end_d>', views.generate_pdf4, name='generate_pdf4'),
    path('payment_type_bank',views.payment_type_bank,name='payment_type_bank'),
    path('generate_pdf5/<str:jsondict>/<str:start_d>/<str:end_d>', views.generate_pdf5, name='generate_pdf5'),
    path('payment_type_bank_get_data', views.payment_type_bank_get_data, name='payment_type_bank_get_data'),
    path('payment_type_upi_get_data', views.payment_type_upi_get_data, name='payment_type_upi_get_data'),
    
    path('get_payment_terms/', views.get_payment_terms_view, name='get_payment_terms'),
    path('get_all_payment_terms/', views.get_all_payment_terms, name='get_all_payment_terms'),
    #path('fetch_payment_terms/', views.fetch_payment_terms, name='fetch_payment_terms'),
    path('get_customer_details/', views.get_customer_details, name='get_customer_details'),
    path('invoice/overview/<int:id>', views.invoice_overview, name='invoice_overview'),
    path('delivery/challan/overview/<int:id>',views.delivery_challan_overview,name='delivery_challan_overview'),
    path('filter_invoice_overview_draft/<int:id>',views.filter_invoice_overview_draft,name='filter_invoice_overview_draft'),
    path('filter_invoice_overview_send/<int:id>',views.filter_invoice_overview_send,name='filter_invoice_overview_send'),
    path('invoice/slip/<int:id>',views.invoice_slip,name='invoice_slip'),
    path('change_status_invoice/<int:id>/', views.change_status_invoice, name='change_status_invoice'),
    
    path('expensebyemployee',views.expensebyemployee,name='expensebyemployee'),
    path('customize_expenseemployee_report',views.customize_expenseemployee_report,name='customize_expenseemployee_report'),
    path('milege',views.milege,name='milege'),
    path('expensebyproject',views.expensebyproject,name='expensebyproject'),
    path('customize_expenseproject_report',views.customize_expenseproject_report,name='customize_expenseproject_report'),
    
    path('nonmilege',views.nonmilege,name='nonmilege'),
    
    path('delivery/challan/slip/<int:id>',views.delivery_challan_slip,name='delivery_challan_slip'),
    
    
    path('chellan/overview/<int:pk>',views.filter_by_draft_chellan_overview,name='filter_by_draft_chellan_overview'),
    path('chellan/overview/<int:pk>',views.filter_by_sent_chellan_overview,name='filter_by_sent_chellan_overview'),
    
    path('convert_challan_to_invoice/<int:id>/', views.convert_challan_to_invoice, name='convert_challan_to_invoice'),
    
    path('custmz_rprt_shw_hide',views.custmz_rprt_shw_hide,name='custmz_rprt_shw_hide'),
    
    #------------------------------------------------------------------------------------------------shamreena---inventory details
    path('productsalereport', views.productsalereport, name='productsalereport'),
    path('inven_salecount', views.inven_salecount, name='inven_salecount'),
    
    path('productsale_filter', views.productsale_filter, name='productsale_filter'),
    path('product_graphview',views.product_graphview,name='product_graphview'),
    path('product_graphview_btn/<str:pk>',views.product_graphview_btn,name='product_graphview_btn'),
    #End
    
    path('holiday_add',views.holiday_add,name='holiday_add'),
    path('holiday_edit/<int:id>',views.holiday_edit,name='holiday_edit'),
    path('edit_holiday/<int:id>',views.edit_holiday,name='edit_holiday'),
    
    path('view_vendor_name',views.view_vendor_name,name='view_vendor_name'),
    path('view_paidthrough',views.view_paidthrough,name='view_paidthrough'),
    path('get_next_reference_number',views.get_next_reference_number,name='get_next_reference_number'),
    path('fetch-bill-data/', views.fetch_bill_data, name='fetch_bill_data'),
    path('update-amount-due/', views.update_amount_due, name='update_amount_due'),
    path('payment_add_details_1',views.payment_add_details_1,name='payment_add_details_1'),
    
    path('pur_rec_customer_dropdown',views.pur_rec_customer_dropdown,name='pur_rec_customer_dropdown'),
    
    path('get_vendor_destination_of_supply', views.get_vendor_destination_of_supply, name='get_vendor_destination_of_supply'),
    
    path('get_cust_pos',views.get_cust_pos,name='get_cust_pos'),
    
    path('customer_dropdown_estimate',views.customer_dropdown_estimate,name='customer_dropdown_estimate'),
    
    path('customer_drpdownrecur',views.customer_dropdownrecur,name='customer_dropdownrecur'),
    path('recuritem',views.recuritem,name='recuritem'),
    
    path('payment_delete_details/', views.payment_delete_details, name='payment_delete_details'),
    
    path('delete_recur_comments/<int:id>/<int:commentid>', views.delete_recur_comments, name='delete_recur_comments'),
    path('delete_cust_comments/<int:id>/<int:commentid>', views.delete_cust_comments, name='delete_cust_comments'),
    path('recur_item_dropdown',views.recur_item_dropdown ,name = 'recur_item_dropdown'),
    
    path('update-opening-balance/', views.update_opening_balance, name='update_opening_balance'),
    
    path('sales_order_details', views.sales_order_details, name='sales_order_details'),
    path('retainer_invoice_details', views.retainer_invoice_details, name='retainer_invoice_details'),
    path('estimate_details', views.estimate_details, name='estimate_details'),
    path('vendor_credits_details',views.vendor_credits_details,name='vendor_credits_details'), 
    
    path('convert_to_recinvoice/<int:pk>',views.convert_to_recinvoice,name='convert_to_recinvoice'),
    path('itemdata_ri', views.itemdata_ri, name='itemdata_ri'),
    
    path('journal_report',views.journal_report,name='journal_report'), 
    path('purchase_order_details',views.purchase_order_details,name='purchase_order_details'),
    
    path('convert_creditnote_status/<int:id>/', views.convert_creditnote_status, name='convert_creditnote_status'),
    path('fetch_invoice_numbers/', views.fetch_invoice_numbers, name='fetch_invoice_numbers'),
    
    #==============================================  ASHIKH VU (start) ==============================================
    
    path('payment_reciedved_list_out', views.payment_reciedved_list_out, name='payment_reciedved_list_out'),
    path('payment_recieved_create', views.payment_recieved_create, name='payment_recieved_create'),
    path('get_customer_details_for_pay_rec', views.get_customer_details_for_pay_rec, name='get_customer_details_for_pay_rec'),
    path('check_payment_num_valid', views.check_payment_num_valid, name='check_payment_num_valid'),
    path('payment_recieved_create_new', views.payment_recieved_create_new, name='payment_recieved_create_new'),
    path('get_bank_acc_num', views.get_bank_acc_num, name='get_bank_acc_num'),
    path('import_payment_recieved', views.import_payment_recieved, name='import_payment_recieved'),
    path('download_pay_rec_sampleImportFile', views.download_pay_rec_sampleImportFile, name='download_pay_rec_sampleImportFile'),
    path('payment_recieved_overview/<int:pk>', views.payment_recieved_overview, name='payment_recieved_overview'),
    path('payment_recieved_view_or_edit/<int:pk>', views.payment_recieved_view_or_edit, name='payment_recieved_view_or_edit'),
    path('payment_recieved_overview_sort_by_name/<int:pk>', views.payment_recieved_overview_sort_by_name, name='payment_recieved_overview_sort_by_name'),
    path('payment_recieved_overview_sort_paynum/<int:pk>', views.payment_recieved_overview_sort_paynum, name='payment_recieved_overview_sort_paynum'),
    path('payment_recieved_update/<int:pk>', views.payment_recieved_update, name='payment_recieved_update'),
    path('payment_recieved_delete/<int:pk>', views.payment_recieved_delete, name='payment_recieved_delete'),
    path('add_comment_payment_recieved/<int:pk>', views.add_comment_payment_recieved, name='add_comment_payment_recieved'),
    path('attatch_file_payment_revieved/<int:pk>', views.attatch_file_payment_revieved, name='attatch_file_payment_revieved'),
    path('payment_recieved_send_mail_page/<int:pk>', views.payment_recieved_send_mail_page, name='payment_recieved_send_mail_page'),
    path('download_pdf_payment_recieved/<int:pk>', views.download_pdf_payment_recieved, name='download_pdf_payment_recieved'),
    
    path('download_ebay_sampleImportFile',views.download_ebay_sampleImportFile,name='download_ebay_sampleImportFile'),
    path('import_eway_list',views.import_eway_list,name='import_eway_list'),
    path('ewaycreate_get_customer_details',views.ewaycreate_get_customer_details,name='ewaycreate_get_customer_details'),
    path('check_eway_num_valid',views.check_eway_num_valid,name='check_eway_num_valid'),
    path('access_vehicle_number',views.access_vehicle_number,name='access_vehicle_number'),
    # path('get_item_hsn_eway',views.get_item_hsn_eway,name='get_item_hsn_eway'),
    path('eway_add_comment/<int:pk>',views.eway_add_comment,name='eway_add_comment'),
    path('ewaysend_mail/<int:pk>',views.ewaysend_mail,name='ewaysend_mail'),
    path('import_eway_bill',views.import_eway_bill,name='import_eway_bill'),

    #==============================================  ASHIKH VU (end) ================================================
    
    path('import_estimate',views.import_estimate,name='import_estimate'),
    path('downloadEstimateSampleImportFile',views.downloadEstimateSampleImportFile,name='downloadEstimateSampleImportFile'),
    path('attach_estimate_file/<int:pk>',views.attach_estimate_file,name='attach_estimate_file'),

    path('filter_by_draft_exp',views.filter_by_draft_exp,name='filter_by_draft_exp'),
    path('filter_by_save_exp',views.filter_by_save_exp,name='filter_by_save_exp'),
    path('exp_sort_by_amount',views.exp_sort_by_amount,name='exp_sort_by_amount'),
    path('exp_sort_by_expen_acc',views.exp_sort_by_expen_acc,name='exp_sort_by_expen_acc'),


    path('exp_view_sort_by_amount/<int:pk>',views.exp_view_sort_by_amount,name='exp_view_sort_by_amount'),
    path('exp_view_sort_by_account/<int:pk>',views.exp_view_sort_by_account,name='exp_view_sort_by_account'),
    path('filter_expense_view_draft/<int:pk>',views.filter_expense_view_draft,name='filter_expense_view_draft'),
    path('filter_expense_view_save/<int:pk>',views.filter_expense_view_save,name='filter_expense_view_save'),


    path('add_exp_comment/<int:pk>',views.add_exp_comment,name='add_exp_comment'),
    path('attach_expense_file/<int:pk>',views.attach_expense_file,name='attach_expense_file'),
    path('expense_status_edit/<int:pk>',views.expense_status_edit,name='expense_status_edit'),
    path('get_account_no',views.get_account_no,name='get_account_no'),


    path('downloadExpenseSampleImportFile',views.downloadExpenseSampleImportFile,name='downloadExpenseSampleImportFile'),
    path('import_expense',views.import_expense,name='import_expense'),
    path('exp_get_customerdet',views.exp_get_customerdet,name='exp_get_customerdet'),
    
    path('sales_order_det_draft/<int:id>',views.sales_order_det_draft,name='sales_order_det_draft'),
    path('sales_order_det_approved/<int:id>',views.sales_order_det_approved,name='sales_order_det_approved'),
    path('invoice_view_draft/<int:pk>',views.invoice_view_draft,name='invoice_view_draft'),
    path('invoice_view_send/<int:pk>',views.invoice_view_send,name='invoice_view_send'),
    path('shareSalesOrderToEmail/<int:id>',views.shareSalesOrderToEmail,name='shareSalesOrderToEmail'),
    path('shareRetInvoiceToEmail/<int:id>',views.shareRetInvoiceToEmail,name='shareRetInvoiceToEmail'),
    path('convert_to_recinvoice_frm_salesorder/<int:pk>',views.convert_to_recinvoice_frm_salesorder,name='convert_to_recinvoice_frm_salesorder'),
    
    path('convert_to_reccinvoice/<int:pk>',views.convert_to_reccinvoice,name='convert_to_reccinvoice'),
    path('item_dropdown_estimate',views.item_dropdown_estimate,name='item_dropdown_estimate'),

    # ---------Bank Holders & Loan account ------------shemeem------------------------------------------------------
    path('bank_holders',views.bankHolders, name = 'bankHolders'),
    path('add_bank_holder',views.addBankHolder, name='addBankHolder'),
    path('new_bank_holder',views.newBankHolder, name='newBankHolder'),
    path('get_bank_details',views.getBankDetails, name='getBankDetails'),
    path('get_all_banks',views.getAllBanks, name='getAllBanks'),
    path('bank_holders_active',views.bankHoldersActive, name='bankHoldersActive'),
    path('bank_holders_inactive',views.bankHoldersInactive, name='bankHoldersInactive'),
    path('bank_holders_sortby_name',views.bankHoldersSortByName, name='bankHoldersSortByName'),
    path('bank_holders_sortby_acc_num',views.bankHoldersSortByAccNum, name='bankHoldersSortByAccNum'),
    path('bank_holder_change_inactive/<int:id>',views.bankHolderStatusInactive, name='bankHolderStatusInactive'),
    path('bank_holder_change_active/<int:id>',views.bankHolderStatusActive, name='bankHolderStatusActive'),
    path('delete_bank_holder/<int:id>',views.deleteBankHolder, name='deleteBankHolder'),
    path('edit_bank_holder/<int:id>',views.editBankHolder, name='editBankHolder'),
    path('update_bank_holder/<int:id>',views.updateBankHolder, name='updateBankHolder'),
    path('view_bank_holder/<int:id>',views.viewBankHolder, name='viewBankHolder'),
    path('holder_name_asc/<int:id>',views.holderNameAsc, name='holderNameAsc'),
    path('holder_name_desc/<int:id>',views.holderNameDesc, name='holderNameDesc'),

    # Loan Account urls
    path('loan_accounts',views.loanAccounts,name='loanAccounts'),
    path('add_loan_account',views.addLoanAccount,name='addLoanAccount'),
    path('get_holder_details',views.getHolderDetails, name='getHolderDetails'),
    path('get_all_bank_holders',views.getAllBankHolders, name='getAllBankHolders'),
    path('create_loan_account',views.createLoanAccount, name='createLoanAccount'),
    path('view_loan_account/<int:id>',views.viewLoanAccount, name= 'viewLoanAccount'),
    path('delete_loan_account/<int:id>',views.deleteLoanAccount, name='deleteLoanAccount'),
    path('edit_loan_account/<int:id>',views.editLoanAccount, name='editLoanAccount'),
    path('update_loan_account/<int:id>',views.updateLoanAccount,name='updateLoanAccount'),
    path('loan_account_active',views.loanAccountActive, name='loanAccountActive'),
    path('loan_account_inactive',views.loanAccountInactive, name='loanAccountInactive'),
    path('loan_account_sortby_name',views.loanAccountSortByName, name='loanAccountSortByName'),
    path('loan_account_sortby_amount',views.loanAccountSortByAmount, name='loanAccountSortByAmount'),
    path('loan_account_change_inactive/<int:id>',views.loanAccountStatusInactive, name='loanAccountStatusInactive'),
    path('loan_account_change_active/<int:id>',views.loanAccountStatusActive, name='loanAccountStatusActive'),
    path('loan_account_name_asc/<int:id>',views.loanAccountNameAsc, name='loanAccountNameAsc'),
    path('loan_account_name_desc/<int:id>',views.loanAccountNameDesc, name='loanAccountNameDesc'),
    path('edit_loan_account_transaction/<int:id>',views.editLoanAccountTransaction, name='editLoanAccountTransaction'),
    path('update_loan_account_transaction/<int:id>',views.updateLoanAccountTransaction, name='updateLoanAccountTransaction'),
    path('delete_loan_account_transaction/<int:id>',views.deleteLoanAccountTransaction, name='deleteLoanAccountTransaction'),
    path('make_emi_payment/<int:id>',views.makeEmiPayment, name='makeEmiPayment'),
    path('get_additional_loan/<int:id>',views.getAdditionalLoan, name='getAdditionalLoan'),
    path('transactionsInBetween/<int:id>',views.transactionsInBetween, name='transactionsInBetween'),
    path('share_loan_account_statement/<int:id>',views.shareLoanAccountStatementToEmail, name='shareLoanAccountStatementToEmail'),
    path('loan_account_statement_pdf/<int:id>',views.loanAccountStatementPdf,name='loanAccountStatementPdf'),

# ---------------------------------------------------------end-----------------------------------------------------

    path('bank_holders_sortby_bank_name',views.bankHoldersSortByBankName, name='bankHoldersSortByBankName'),
    path('check_holder_name',views.checkHolderName, name='checkHolderName'),
    
    #................................  URls START............ Godown details & project details & GSTR9...... TINTO MT .......( start )......................

    path('godown_details', views.godown_details, name='godown_details'),
    path('shareGodownDetailsToEmail', views.shareGodownDetailsToEmail, name='shareGodownDetailsToEmail'),
    path('project_details', views.project_details, name='project_details'),
    path('GSTR_9page', views.GSTR_9page, name='GSTR_9page'),
    path('shareGSTR9ToEmail', views.shareGSTR9ToEmail, name='shareGSTR9ToEmail'),
    path('GSTR9pdfs', views.GSTR9pdfs, name='GSTR9pdfs'),
#................................  Views END ............ Godown details & project details & GSTR9...... TINTO MT .......( end )......................

    path('import_employee_loan_details',views.import_employee_loan_details,name='import_employee_loan_details'), 
    path('import_employee_details',views.import_employee_details,name='import_employee_details'),
    path('share_loan_email/<int:id>',views.share_loan_email,name='share_loan_email'), 
    path('create_loan_duration',views.create_loan_duration,name='create_loan_duration'), 

    path('loan_duration',views.loan_duration,name='loan_duration'), 

    
    path('repayment_view/<int:id>', views.repayment_view, name='repayment_view'),
    path('add_repayment/<int:id>', views.add_repayment, name='add_repayment'),
    path('additional_loan_view/<int:id>', views.additional_loan_view, name='additional_loan_view'), 
    path('add_additional_loan/<int:id>', views.add_additional_loan, name='add_additional_loan'), 
    path('delete_repayment/<int:id>', views.delete_repayment, name='delete_repayment'), 
    path('edit_repayment_view/<int:id>', views.edit_repayment_view, name='edit_repayment_view'), 
    path('edit_repayment/<int:id>', views.edit_repayment, name='edit_repayment'), 
    path('edit_additional_loan_view/<int:id>', views.edit_additional_loan_view, name='edit_additional_loan_view'), 
    path('edit_additional_loan/<int:id>', views.edit_additional_loan, name='edit_additional_loan'),  
    
    path('purchaseOrderDetailsToEmail',views.purchaseOrderDetailsToEmail,name='purchaseOrderDetailsToEmail'),
    path('JournalReportToEmail',views.JournalReportToEmail,name='JournalReportToEmail'),
    
    #==============================================  ASHIKH VU (start) ==============================================
    
    path('payment_recieved_to_mail/<int:pk>',views.payment_recieved_to_mail,name='payment_recieved_to_mail'),
    path('ewaybill_to_mail/<int:pk>',views.ewaybill_to_mail,name='ewaybill_to_mail'),

    #==============================================  ASHIKH VU (end) ================================================
    
    path('shareEstimateToEmail/<int:pk>',views.shareEstimateToEmail,name='shareEstimateToEmail'),
    path('shareExpenseToEmail/<int:pk>',views.shareExpenseToEmail,name='shareExpenseToEmail'),
    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    



    path('create_account2',views.create_account2,name='create_account2'),
    path('entr_custmrA2',views.entr_custmrA2,name='entr_custmrA2'),
      path('shareProjectToEmail/<int:pk>',views.shareProjectToEmail,name='shareProjectToEmail'),
    path('edit_project/<int:project_id>',views.edit_project,name='edit_project'),
        path('deletp/<int:id>',views.deletp,name='deletp'),
          path('attach_project_file/<int:pk>',views.attach_project_file,name='attach_project_file'),
  path('downloadProjectSampleImportFile',views.downloadProjectSampleImportFile,name='downloadProjectSampleImportFile'),
    path('import_project',views.import_project,name='import_project'),
     path('add_vendort/',views.add_vendort,name='add_vendort'),
     
      path('projectcust',views.projectcust,name='projectcust'),
        path('entr_custmrApro', views.entr_custmrApro, name='entr_custmrApro'),



        path('expensevendor', views.expensevendor, name='expensevendor'),

         path('entr_custmrA3',views.entr_custmrA3,name='entr_custmrA3'),



# path('vendordata', views.vendordata, name='vendordata'),
      path('exp_get_vendordet',views.exp_get_vendordet,name='exp_get_vendordet'),
       path('exp_get_employeedet', views.exp_get_employeedet, name='exp_get_employeedet'),








      #  ====new====

       path('create_emp1', views.create_emp1, name='create_emp1'),

    
           path('overviewbillable/<int:id>',views.overviewbillable,name='overviewbillable'),
            path('overviewnonbillable/<int:id>',views.overviewnonbillable,name='overviewnonbillable'),
             path('entr_custmrApro',views.entr_custmrApro,name='entr_custmrApro'),


    








# new

      path('new_emp',views.new_emp,name='new_emp'),

        path('emp_dropdownE/', views.emp_dropdownE, name='emp_dropdownE'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)