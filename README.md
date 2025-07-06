# PG2_PRACTICA5

# 1. Patrón Factory 

## ¿Qué es y Por Qué se Usó?

El Patrón Factory se utilizó para crear objetos de café base (como Espresso, Americano o Latte) de manera centralizada, sin que el código que los solicita necesite saber los detalles de cómo se crean. Esto se hizo para desacoplar el código cliente de la lógica de creación, facilitando la adición de nuevos tipos de café en el futuro sin modificar el código existente.

## ¿Dónde está implementado en el código?

Está implementado en el archivo pedidos_cafe/factory.py con la clase CafeFactory y su método estático obtener_base(tipo). Las clases de café base (Espresso, Americano, Latte) están definidas en pedidos_cafe/base.py.

## ¿Cómo se prueba o evidencia su uso?

Su uso se evidencia en pedidos_cafe/serializers.py, donde la línea cafe = CafeFactory.obtener_base(obj.tipo_base) invoca la fábrica para obtener la instancia de café base correcta según el tipo de pedido.

# 2. Patrón Builder 

## ¿Qué es y Por Qué se Usó?

El Patrón Builder se utilizó para construir objetos PedidoCafe complejos paso a paso, como añadir ingredientes y ajustar el tamaño. Esto permite una construcción flexible y separa la lógica de cómo se construye un café de su representación final, lo que es útil para crear pedidos personalizados o "paquetes" predefinidos.

## ¿Dónde está implementado en el código?

Está implementado en el archivo pedidos_cafe/builder.py, que contiene las clases CafePersonalizadoBuilder (el constructor) y CafeDirector (el director que orquesta los pasos de construcción).

## ¿Cómo se prueba o evidencia su uso?

Su uso se observa en pedidos_cafe/serializers.py, específicamente en el método auxiliar _build_cafe_and_get_builder. Este método muestra cómo el Director utiliza los pasos definidos en el Builder para ensamblar el café personalizado, calculando su precio y sus ingredientes finales.

# 3. Patrón Singleton (Instancia Única)

## ¿Qué es y Por Qué se Usó?

El Patrón Singleton se utilizó para asegurar que la clase Logger tenga una única instancia global en toda la aplicación. Esto proporciona un punto centralizado para registrar mensajes y operaciones, lo cual es ideal para gestionar logs y otros recursos globales.

## ¿Dónde está implementado en el código?

Está implementado en el archivo api_patrones/logger.py con la clase Logger. La lógica para asegurar una única instancia se encuentra en el método especial __new__ de esta clase.

## ¿Cómo se prueba o evidencia su uso?

Su uso se evidencia en pedidos_cafe/serializers.py, donde cada vez que se necesita registrar una operación (por ejemplo, el cálculo del precio), se llama a Logger().registrar(...). Esto demuestra que siempre se accede a la misma instancia del Logger para almacenar todos los mensajes.