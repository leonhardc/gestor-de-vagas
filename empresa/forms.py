
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Fieldset,
    Row,
    Column,
    HTML,
)

from .models import Vaga, Empresa


class VagaForm(forms.ModelForm):

    class Meta:
        model = Vaga

        fields = [
            "empresa",
            "titulo",
            "descricao",
            "url_vaga",
            "modelo_de_trabalho",
            "tipo_de_emprego",
            "encontrado_em",
            "requisitos",
            "salario",
            "localizacao",
        ]

        widgets = {
            "empresa": forms.Select(),

            "titulo": forms.TextInput(attrs={
                "placeholder": "Ex.: Desenvolvedor Python Júnior"
            }),

            "descricao": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Descrição da oportunidade..."
            }),

            "url_vaga": forms.URLInput(attrs={
                "placeholder": "https://..."
            }),

            "requisitos": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Conhecimentos, habilidades e requisitos..."
            }),

            "salario": forms.NumberInput(attrs={
                "placeholder": "Ex.: 3500.00",
                "step": "0.01",
                "min": "0"
            }),

            "localizacao": forms.TextInput(attrs={
                "placeholder": "Ex.: Fortaleza - CE"
            }),
        }

    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Filtra as empresas pertencentes ao usuário
        self.fields["empresa"].queryset = Empresa.objects.none()

        if usuario is not None:
            self.fields["empresa"].queryset = Empresa.objects.filter(
                usuario=usuario
            ).order_by("nome")

        self.fields["empresa"].empty_label = "Selecione uma empresa"

        # Configuração Crispy Forms
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = True

        self.helper.layout = Layout(

            Fieldset(
                "Informações da oportunidade",

                "empresa",

                "titulo",

                "descricao",

                "requisitos",
            ),

            HTML('<hr class="my-4">'),

            Fieldset(
                "Detalhes da vaga",

                Row(
                    Column(
                        "modelo_de_trabalho",
                        css_class="col-md-6"
                    ),
                    Column(
                        "tipo_de_emprego",
                        css_class="col-md-6"
                    ),
                ),

                Row(
                    Column(
                        "salario",
                        css_class="col-md-6"
                    ),
                    Column(
                        "localizacao",
                        css_class="col-md-6"
                    ),
                ),
            ),

            HTML('<hr class="my-4">'),

            Fieldset(
                "Origem da oportunidade",

                Row(
                    Column(
                        "encontrado_em",
                        css_class="col-md-6"
                    ),
                    Column(
                        "url_vaga",
                        css_class="col-md-6"
                    ),
                ),
            ),
        )
