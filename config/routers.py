class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'movie':
            return 'movies'
        
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'movie':
            return 'movies'
        
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ("movie", "default")

        if obj1._meta.app_label in db_list or obj2._meta.app_label in db_list:
            return True
        
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'movie':
            return db == 'movies'
        
        return db == 'default'
    