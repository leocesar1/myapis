class ExamsRouter:
    """
    Um router para controlar todas as operações de banco de
    dados dos models da app auth.
    """
    def db_for_read(self, model, **hints):
        """
        Definição do nome do banco para leitura.
        """
        if model._meta.app_label == 'exams':
            return 'exams'
        return None

    def db_for_write(self, model, **hints):
        """
        Definição do nome do banco para escrita.
        """
        if model._meta.app_label == 'exams':
            return 'exams'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Permite relações se um model na app auth está envolvido.
        """
        if obj1._meta.app_label == 'exams' or \
           obj2._meta.app_label == 'exams':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Certifica que a app auth aparece apenas no banco 'auth_db'.
        database.
        """
        if app_label == 'exams':
            return db == 'exams'
        return None