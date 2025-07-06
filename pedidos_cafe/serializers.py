from rest_framework import serializers
from pedidos_cafe.models import PedidoCafe
from pedidos_cafe.factory import CafeFactory
from pedidos_cafe.builder import CafePersonalizadoBuilder, CafeDirector
from apipatrones.logger import Logger


class PedidoCafeSerializer(serializers.ModelSerializer):
    precio_total = serializers.SerializerMethodField()
    ingredientes_finales = serializers.SerializerMethodField()

    class Meta:
        model = PedidoCafe
        fields = [
            "id",
            "cliente",
            "tipo_base",
            "ingredientes",
            "tamanio",
            "fecha",
            "precio_total",
            "ingredientes_finales",
        ]

    INGREDIENTE_PRECIOS = {
        "canela": 1,
        "chocolate": 2,
        "vainilla": 1.5,
        "azucar": 0.5,
        "leche extra": 2,
        "leche": 1,
    }

    def validate_ingredientes(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Los ingredientes deben ser una lista.")
        
        for ingrediente in value:
            if not isinstance(ingrediente, str):
                raise serializers.ValidationError("Cada ingrediente en la lista debe ser un texto.")
            if ingrediente not in self.INGREDIENTE_PRECIOS:
                raise serializers.ValidationError(
                    f"Ingrediente '{ingrediente}' no válido o no disponible. "
                    f"Los permitidos son: {', '.join(self.INGREDIENTE_PRECIOS.keys())}"
                )
        return value

    def _build_cafe_and_get_builder(self, obj):
        cafe = CafeFactory.obtener_base(obj.tipo_base)
        
        builder = CafePersonalizadoBuilder(cafe)
        director = CafeDirector(builder)
        
        ingredientes_a_procesar = obj.ingredientes if isinstance(obj.ingredientes, list) else []
        
        director.construir(ingredientes_a_procesar, obj.tamanio)
        
        return builder

    def get_precio_total(self, obj):

        builder = self._build_cafe_and_get_builder(obj)
        Logger().registrar(f"Se registró el cálculo del precio para el pedido {obj.id}")
        return builder.obtener_precio()

    def get_ingredientes_finales(self, obj):
        builder = self._build_cafe_and_get_builder(obj)
        Logger().registrar(
            f"Se registró la obtención de ingredientes finales para el pedido {obj.id}"
        )
        return builder.obtener_ingredientes_finales()