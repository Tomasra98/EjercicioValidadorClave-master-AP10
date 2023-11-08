from abc import ABC, abstractmethod
from validadorclave.modelo.errores import (LongitudInvalidaError,
SinMayusculaError,
SinMinusculaError,
SinNumeroError,
SinCaracterEspecialError,
SinCalistoError
)

class ReglaValidacion(ABC):
  def _init_(self, longitud_esperada):
      self.longitud_esperada = longitud_esperada

  @abstractmethod
  def es_valida(self, clave):
      pass

  def _validar_longitud(self, clave):
      if len(clave) <= self.longitud_esperada:
          raise LongitudInvalidaError("La longitud de la clave no cumple con lo esperado.")

  def _contiene_mayuscula(self, clave):
      if not any(c.isupper() for c in clave):
          raise SinMayusculaError("La clave debe contener al menos una letra mayúscula.")

  def _contiene_minuscula(self, clave):
      if not any(c.islower() for c in clave):
          raise SinMinusculaError("La clave debe contener al menos una letra minúscula.")

  def _contiene_numero(self, clave):
      if not any(c.isdigit() for c in clave):
          raise SinNumeroError("La clave debe contener al menos un número.")

class ReglaValidacionGanimedes(ReglaValidacion):
  def _init_(self):
      super()._init_(8)

  def contiene_caracter_especial(self, clave):
      caracteres_especiales = '@_#$%'
      if not any(c in caracteres_especiales for c in clave):
          raise SinCaracterEspecialError("La clave debe contener al menos un carácter especial: @, _, #, $ o %.")

  def es_valida(self, clave):
      super()._validar_longitud(clave)
      super()._contiene_mayuscula(clave)
      super()._contiene_minuscula(clave)
      super()._contiene_numero(clave)
      self.contiene_caracter_especial(clave)
      return True

class ReglaValidacionCalisto(ReglaValidacion):
  def _init_(self):
      super()._init_(6)

  def contiene_calisto(self, clave):
      if "calisto" in clave.lower():
          return True
      raise SinCalistoError("La clave debe contener la palabra 'calisto' escrita con al menos dos letras mayúsculas, pero no todas.")

  def es_valida(self, clave):
      super()._validar_longitud(clave)
      super()._contiene_numero(clave)
      self.contiene_calisto(clave)
      return True

class Validador:
  def _init_(self, regla):
      self.regla = regla

  def es_valida(self, clave):
      return self.regla.es_valida(clave)