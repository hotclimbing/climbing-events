from django.urls import path

from events import views, pay_views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('e/<int:event_id>/', views.EventView.as_view(), name='event'),
    path('e/<int:event_id>/admin_actions/', views.AdminActionsView.as_view(), name='admin_actions'),
    path('e/<int:event_id>/admin_description/', views.AdminDescriptionView.as_view(),
         name='admin_description'),
    path('e/<int:event_id>/admin_settings/', views.AdminSettingsView.as_view(), name='admin_settings'),
    path('e/<int:event_id>/admin_protocols', views.AdminProtocolsView.as_view(), name='admin_protocols'),
    path('e/<int:event_id>/admin_protocols/<str:file>', views.ProtocolDownload.as_view(), name='protocol_download'),
    path('e/<int:event_id>/admin_protocols/<str:file>/remove', views.ProtocolRemove.as_view(), name='protocol_remove'),
    path('async_get_results/<int:event_id>/', views.async_get_results, name='async_get_results'),
    path('e/<int:event_id>/enter/', views.EnterResultsView.as_view(), name='enter_results'),
    path('e/<int:event_id>/enter_ok/', views.EnterResultsOKView.as_view(), name='enter_results_ok'),
    path('e/<int:event_id>/enter_check/', views.EnterCheckView.as_view(), name='enter_check'),
    path('e/<int:event_id>/enter_wo_reg/', views.EnterWithoutReg.as_view(), name='enter_wo_reg'),
    path('e/<int:event_id>/results/', views.ResultsView.as_view(), name='results'),
    path('e/<int:event_id>/participants/', views.ParticipantsView.as_view(), name='participants'),
    path('e/<int:event_id>/registration/', views.RegistrationView.as_view(), name='registration'),
    path('e/<int:event_id>/registration_ok/<int:participant_id>', views.EventRegistrationOkView.as_view(),
         name='event_registration_ok'),
    path('e/<int:event_id>/route_editor/', views.RouteEditor.as_view(), name='route_editor'),
    path('e/<int:event_id>/p/<int:p_id>/', views.ParticipantView.as_view(), name='participant'),
    path('e/<int:event_id>/p/<int:p_id>/routes', views.ParticipantRoutesView.as_view(), name='participant_routes'),
    path('e/<int:event_id>/p/<int:p_id>/remove', views.ParticipantRemoveView.as_view(), name='participant_remove'),

    path('create/', views.CreateEventView.as_view(), name='create'),
    path('my_events/', views.MyEventsView.as_view(), name='my_events'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('help/', views.HelpView.as_view(), name='help'),

    path('ajax/check_pin_code/', views.check_pin_code, name='check_pin_code'),

    path('pay/notify/', pay_views.NotifyView.as_view(), name='pay_notify'),
    path('pay/notify/', pay_views.notify, name='pay_notify2'),

    path('pay/<int:event_id>/<int:p_id>/', pay_views.CreatePay.as_view(), name='pay_create'),
    path('pay/ok/<int:event_id>/', pay_views.PayOk.as_view(), name='pay_ok'),

    path('test/', views.async_get_results, name='test'),
]
