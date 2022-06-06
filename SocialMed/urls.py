from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.http import Http404, HttpResponseServerError
from django.urls import include, path, re_path
from drf_yasg import openapi
# Swagger
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

schema_view = get_schema_view(
    openapi.Info(
        title="Social Med's API",
        description="Social Med API",
        default_version="v1",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="xackercoder@gmail.com@gmail.com"),
        license=openapi.License(name="MetSenat License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/news/", include("api.v1.news.urls")),
    path("api/v1/maps/", include("api.v1.maps.urls")),
    path("api/v1/services/", include("api.v1.services.urls")),
    # Swagger UI documentation
    re_path(
        r"^api/swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^api/swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^api/redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    # login and register JWT
    # path('api/token/register/', RegisterApi.as_view(), name='api_register'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("i18n/", include("django.conf.urls.i18n")),
    path("__debug__/", include("debug_toolbar.urls")),
]
# translate
urlpatterns += i18n_patterns(
    path("api/v1/news/", include("api.v1.news.urls")),
    path("api/v1/maps/", include("api.v1.maps.urls")),
    path("api/v1/services/", include("api.v1.services.urls")),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Error handlers
handler404 = lambda request, exception: Http404("Not found")
handler500 = lambda request: HttpResponseServerError("Internal Server Error")
