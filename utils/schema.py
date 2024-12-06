from drf_yasg import openapi


QUERY_RECOMMENDATION_ID = openapi.Parameter(
    'recommendation_id', openapi.IN_QUERY,
    description='1',
    type=openapi.TYPE_INTEGER,
    required=True
)

QUERY_SERVICE_ID = openapi.Parameter(
    'service_id', openapi.IN_QUERY,
    description='1',
    type=openapi.TYPE_INTEGER,
    required=True
)

QUERY_DIRECTION = openapi.Parameter(
    'direction', openapi.IN_QUERY,
    description='1',
    type=openapi.TYPE_INTEGER,
)

QUERY_COUNTRY_IDS = openapi.Parameter(
    'countries',
    openapi.IN_QUERY,
    description='Example: [1, 2, 3]',
    items=openapi.Items(type=openapi.TYPE_INTEGER),
    type=openapi.TYPE_ARRAY
)

QUERY_TAG_IDS = openapi.Parameter(
    'tags',
    openapi.IN_QUERY,
    description='Example: [1, 2, 3]',
    items=openapi.Items(type=openapi.TYPE_INTEGER),
    type=openapi.TYPE_ARRAY
)

QUERY_SEASON_IDS = openapi.Parameter(
    'seasons',
    openapi.IN_QUERY,
    description='Example: [1, 2, 3]',
    items=openapi.Items(type=openapi.TYPE_INTEGER),
    type=openapi.TYPE_ARRAY
)

QUERY_PLACEMENT_IDS = openapi.Parameter(
    'placements',
    openapi.IN_QUERY,
    description='Example: [1, 2, 3]',
    items=openapi.Items(type=openapi.TYPE_INTEGER),
    type=openapi.TYPE_ARRAY
)

QUERY_FORMATS_IDS = openapi.Parameter(
    'formats',
    openapi.IN_QUERY,
    description='Example: [1, 2, 3]',
    items=openapi.Items(type=openapi.TYPE_INTEGER),
    type=openapi.TYPE_ARRAY
)
