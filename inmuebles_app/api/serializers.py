from rest_framework import serializers
from inmuebles_app.models import Edificacion, Empresa, Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    comentario_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comentario
        exclude = ['edificacion']


class EdificacionSerializer(serializers.ModelSerializer):
    #longitud_direccion = serializers.SerializerMethodField()
    comentarios = ComentarioSerializer(many=True, read_only=True)
    class Meta:
        model = Edificacion
        fields = "__all__"
        #fields = ["id", "pais", "descripcion", "imagen"]
        #exclude = ["id"]
        
    '''def get_longitud_direccion(self, object):
        cantidad_caracteres = len(object.direccion)
        return cantidad_caracteres
        
    def validate(self, data):
        if data['direccion'] == data['pais']:
            raise serializers.ValidationError("La dirección y el país deben ser diferentes")
        else:
            return data
        
    def validate_imagen(self, data):
        if len(data) < 2:
            raise serializers.ValidationError("La urg de la imagen es muy corta")
        else:
            return data'''


class EmpresaSerializer(serializers.ModelSerializer):
    edificacion_list = EdificacionSerializer(many=True, read_only=True)
    #edificacion_list = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #edificacion_list = serializers.StringRelatedField(many=True, read_only=True)
    #edificacion_list = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="edificacion-detail")
    class Meta:
        model = Empresa
        fields = "__all__"


'''def column_longitud(value):
    if len(value) < 2:
        raise serializers.ValidationError("El valor es demasiado corta")
    

class InmuebleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    direccion = serializers.CharField(validators=[column_longitud])
    pais = serializers.CharField(validators=[column_longitud])
    descripcion = serializers.CharField()
    imagen = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self, data):
        return Inmueble.objects.create(**data)
    
    def update(self, inmueble, data):
        inmueble.direccion = data.get('direccion', inmueble.direccion)
        inmueble.pais = data.get('pais', inmueble.pais)
        inmueble.descripcion = data.get('descripcion', inmueble.descripcion)
        inmueble.imagen = data.get('imagen', inmueble.imagen)
        inmueble.active = data.get('active', inmueble.active)
        inmueble.save()
        
        return inmueble
    
    def validate(self, data):
        if data['direccion'] == data['pais']:
            raise serializers.ValidationError("La dirección y el país deben ser diferentes")
        else:
            return data
        
    def validate_imagen(self, data):
        if len(data) < 2:
            raise serializers.ValidationError("La urg de la imagen es muy corta")
        else:
            return data'''