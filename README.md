# django-gibberish
learning to integrate django with celery and django-rest-api and redis

# thigs to be improved

- Add more methods to the tasks to avoid databases operations from blocking the responses.
- Add tests
- Refactor a lot of things
- Enable objects to be created without referencing existing structures
 - As: if we send a `{"nome_da_clinica": "test", "medicos": [{"nome_do_medico": "test", "crm": "9999"}]}`, the `medicos` does not needs to reference a existing Clinica because they will be created together.
- Treat nested objects as not required. We need to be able to create a Clinica with Medicos but not Pacientes.
