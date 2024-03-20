
def get_swagger_spec():
    spec = {
        "swagger": "2.0",
        "info": {
            "title": "E-commerce API",
            "description": "API for managing e-commerce products",
            "version": "1.0.0"
        },
        "basePath": "/",
        "schemes": [
            "http"
        ],
        "tags": [
            {
                "name": "products",
                "description": "Operations related to products"
            }
        ],
        "paths": {
            "/products": {
                "get": {
                    "tags": ["products"],
                    "summary": "Get all products",
                    "responses": {
                        "200": {
                            "description": "List of products",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "products": {
                                        "type": "array",
                                        "items": {
                                            "$ref": "#/definitions/Product"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "post": {
                    "tags": ["products"],
                    "summary": "Create a new product",
                    "parameters": [
                        {
                            "name": "body",
                            "in": "body",
                            "required": True,
                            "schema": {
                                "$ref": "#/definitions/ProductInput"
                            }
                        }
                    ],
                    "responses": {
                        "201": {
                            "description": "Product created successfully"
                        }
                    }
                }
            },
            "/products/{product_id}": {
                "get": {
                    "tags": ["products"],
                    "summary": "Get a product by ID",
                    "parameters": [
                        {
                            "name": "product_id",
                            "in": "path",
                            "required": True,
                            "type": "integer"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Product found",
                            "schema": {
                                "$ref": "#/definitions/Product"
                            }
                        },
                        "404": {
                            "description": "Product not found"
                        }
                    }
                },
                "put": {
                    "tags": ["products"],
                    "summary": "Update a product by ID",
                    "parameters": [
                        {
                            "name": "product_id",
                            "in": "path",
                            "required": True,
                            "type": "integer"
                        },
                        {
                            "name": "body",
                            "in": "body",
                            "required": True,
                            "schema": {
                                "$ref": "#/definitions/ProductInput"
                            }
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Product updated successfully"
                        },
                        "404": {
                            "description": "Product not found"
                        }
                    }
                },
                "delete": {
                    "tags": ["products"],
                    "summary": "Delete a product by ID",
                    "parameters": [
                        {
                            "name": "product_id",
                            "in": "path",
                            "required": True,
                            "type": "integer"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Product deleted successfully"
                        },
                        "404": {
                            "description": "Product not found"
                        }
                    }
                }
            }
        },
        "definitions": {
            "Product": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    },
                    "price": {
                        "type": "number"
                    },
                    "description": {
                        "type": "string"
                    }
                }
            },
            "ProductInput": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "price": {
                        "type": "number"
                    },
                    "description": {
                        "type": "string"
                    }
                },
                "required": ["name", "price", "description"]
            }
        }
    }
    return spec
