from clasepersonal import personal

class docente(personal):
    cargos = ['simple', 'exclusivo']
    _carrera = ''
    _cargo = ''
    _catedra = ''
    porcentajesimple = 0.1
    porcentajesemiexlusivo = 0.2
    porcentajesemiexlusivo = 0.3

    def __init__(self, cuil='', apellido='', nombre='', basico=0, antiguedad=0, carrera='', cargo='', catedra='',
                 area='', tipo=''):
        super().__init__(cuil, apellido, nombre, basico, antiguedad, carrera, cargo, catedra, area, tipo)
        self._carrera = carrera
        self._cargo = cargo
        self._catedra = catedra
    def catedra(self):
        return self.catedra()

    def mostrardatos(self):
       super().mostrardatos()
       print(self._carrera)
       print(self._cargo)
       print(self._catedra)

    def getcarrera(self):
      self._carrera

    def gettipo(self):
        return 'Docente'
    @classmethod
    def getporcentajesimple(cls):
        return cls.porcentajesimple
    @classmethod
    def getporcentajesemiexclusivo(cls):
        return cls.porcentajesemiexlusivo
    @classmethod
    def getporcentajeexclusivo(cls):
        return cls.porcentajesemiexlusivo
    
    @classmethod
    def setporcentajesimple(cls,porcentaje):
        cls.porcentajesimple = porcentaje
    @classmethod
    def setporcentajesemi(cls,porcentaje):
        cls.porcentajesemiexlusivo = porcentaje
    @classmethod
    def setporcentajeexclusivo(cls,porcentaje):
        cls.porcentajeexclusivo = porcentaje        
    
    def calcsueldo(self):
     sueldo = float(self._basico) * (1.0 + 0.01 * float(self._antiguedad))
     if self._cargo.lower() == 'simple':
      sueldo += float(docente.getporcentajesimple()) * float(self._basico)
     elif self._cargo.lower() == 'semiexclusivo':
      sueldo += float(docente.getporcentajesemiexclusivo()) * float(self._basico)
     else:
      sueldo += float(docente.getporcentajeexclusivo()) * float(self._basico)
     return round(sueldo, 2)

    def toJSON(self):
        dic = super().toJSON()
        dic['clase'] = self.__class__.__name__
        atribDocente = dict(
            carrera=self._carrera,
            cargo=self._cargo,
            catedra=self._catedra)
        dic['atributos'].update(atribDocente)
        return dic
