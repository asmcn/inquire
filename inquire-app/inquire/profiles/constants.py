from django.utils.translation import ugettext_lazy as _

FACEBOOK_GRAPH_API_DEBUG_TOKEN_RESOURCE = "https://graph.facebook.com/v2.2/debug_token/"

# Maybe extends here
SERVICE_CHOICE_FACEBOOK = "facebook"

SERVICE_CHOICES = (
    (SERVICE_CHOICE_FACEBOOK, _("Facebook")),
)

