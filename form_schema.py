schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",

    "$id": "location.schema",

    "title": "GMAP package metadata schema",
    "description": "GMAP data packages are summarized by a set of metadata, defined here.",

    "required": [
        "lat_min",
        "lon_west",
        "lat_max",
        "lon_east",
        "target_body",
        "gmap_id",
        "crs"
    ],

    "type": "object",

    "properties": {

        "gmap_id": {
            "type": "string",
            "minLength": 2
        },
        "title": {
            "type": "string"
        },
        "target_body": {
            "type": "string",
            "enum": ["mars", "mercury", "moon"]
        },
        "map_type": {
            "type": "string"
        },
        "crs": {
            "type": "string",
            "minLength": 2,
            "description": "CRS used in the data"
        },
        "lat_min": {
            "type": "number",
            "description": "Minimum latitude in degress",
            "minimum": -90,
            "maximum": 90
        },
        "lat_max": {
            "type": "number",
            "description": "Maximum latitude in degress",
            "minimum": -90,
            "maximum": 90
        },
        "lon_west": {
            "type": "number",
            "description": "West (minimum) longitude in degress",
            "minimum": 0,
            "maximum": 360
        },
        "lon_east": {
            "type": "number",
            "description": "East (maximum) longitude in degress",
            "minimum": 0,
            "maximum": 360
        },
        "output_scale": {
            "type": "string"
        },
        "authors": {
            "type": "string"
        },
        "source_data": {
            "type": "string"
        },
        "standards": {
            "type": "string"
        },
        "doi": {
            "type": "string"
        },
        "references": {
            "type": "string"
        },
        "aims": {
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "relared_products": {
            "type": "string"
        },
        "units_definition": {
            "type": "string"
        },
        "stratigraphic_info": {
            "type": "string"
        },
        "comments": {
            "type": "string"
        },
        "heritage": {
            "type": "string"
        },
        "acknowlegments": {
            "type": "string"
        }
    }
}
