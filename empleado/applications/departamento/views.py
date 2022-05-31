#----------------------------FORM VIEW------------------------------------------





# Create your views here.
#Form view
from django.views.generic.edit import FormView


from .forms import NewDepartamentoForm
#Tablas que se usaran para hacer ls insercion
from applications.persona.models import Empleado
from .models import Departamento


class NewDepartamentoView(FormView):
    template_name="departamento/new_departamento.html"
    form_class=NewDepartamentoForm
    success_url="/"

    def form_valid(self,form):
        '''
        recupera la informacion del formulario 
        y lo ingresa en dos tablas diferentes
        '''
       
        depa=Departamento(
            name=form.cleaned_data["departamento"],
            shortname=form.cleaned_data["shortname"],
            )
        depa.save()


        name=form.cleaned_data["nombre"]
        last_name=form.cleaned_data["apellidos"]
        Empleado.objects.create(first_name=name,
                                last_name=last_name,
                                job="1",
                                #iguala el valor de este campo a lo que se ingreso en departamento
                                departamento=depa)
        
        return super(NewDepartamentoView,self).form_valid(form)
