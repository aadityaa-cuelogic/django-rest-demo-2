from rest_framework import serializers, viewsets
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# class SnippetSerializer(serializers.Serializer):
# 	id = serializers.IntegerField(read_only=True)
# 	title = serializers.CharField(required=False, allow_blank=True,
# 									max_length=100)
# 	code = serializers.CharField(style={'base_template':'textarea.html'})
# 	linenos = serializers.BooleanField(required=False)
# 	language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python')
# 	style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

# 	def create(self, validated_data):
# 		"""
# 		Create and return a new `Snippet` instance, given the validated data.
# 		"""
# 		return Snippet.objects.create(**validated_data)

# 	def update(self, instance, validated_data):
# 		"""
# 		Update and return an existing `Snippet` instance, given the validated data.
# 		"""
# 		instance.title = validated_data.get('title', instance.title)
# 		instance.code = validated_data.get('code', instance.code)
# 		instance.linenos = validated_data.get('linenos', instance.linenos)
# 		instance.language = validated_data.get('language', instance.language)
# 		instance.style = validated_data.get('style', instance.style)
# 		instance.save()
# 		return instance

class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snippet
		# field = ('id', 'title', 'code', 'linenos', 'language', 'style',)
		fields = '__all__'

		# Following error is shown if __all__ is not used
		# AssertionError: (u"Creating a ModelSerializer without either the 'fields' 
		# attribute or the 'exclude' attribute has been deprecated since 3.3.0, and is now disallowed.
		# Add an explicit fields = '__all__' to the SnippetSerializer serializer.",)

class SnippetsViewSet(viewsets.ModelViewSet):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer