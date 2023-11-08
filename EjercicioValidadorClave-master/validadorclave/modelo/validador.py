from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, clave):
        pass

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada
    
    def _contiene_mayuscula(self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)
    
class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init()

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            return False
        if not self._contiene_mayuscula(clave):
            return False
        if not self._contiene_minuscula(clave):
            return False
        if not self._contiene_numero(clave):
            return False
        if not self.contiene_caracter_especial(clave):
            return False
        return True

    def contiene_caracter_especial(self, clave):
        caracteres_especiales = ['@', '_', '#', '$', '%']
        return any(caracter in clave for caracter in caracteres_especiales)


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init()

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            return False
        if not self._contiene_numero(clave):
            return False
        if not self.contiene_calisto(clave):
            return False
        return True

    def contiene_calisto(self, clave):
        calisto_index = clave.lower().find("calisto")
        if calisto_index != -1:
            count_upper = sum(1 for char in clave[calisto_index:calisto_index + 7] if char.isupper())
            if count_upper >= 2 and count_upper < 7:
                return True
        return False
    
class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        return self.regla.es_valida(clave)