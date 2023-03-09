from rest_framework.viewsets import GenericViewSet


class ApiViewSet(GenericViewSet):

    def perform_authentication(self, request):
        return
