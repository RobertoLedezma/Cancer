from cancer import predict_fractal_dimension_worst
def predict_cual_consideras_que_es_el_tipo_de_cancer_que_mas_se_presenta_(edad=None,
                                                                          sexo=None,
                                                                          peso=None,
                                                                          estatura=None,
                                                                          _has_tenido_algun_familiar_con_cancer_=None,
                                                                          _cuantos_familiares_=None,
                                                                          marca_temporal_second=None,
                                                                          marca_temporal_minute=None,
                                                                          marca_temporal_hour=None):
    """ Predictor for ¿Cuál consideras que es el tipo de cáncer que más se presenta? from model/60723846f5aa20482e080d6d

        Predictive model by BigML - Machine Learning Made Easy
    """
    if (marca_temporal_hour is None):
        return u'Mama'
    if (marca_temporal_hour > 14):
        if (peso is None):
            return u'Mama'
        if (peso > 60):
            if (marca_temporal_minute is None):
                return u'Mama'
            if (marca_temporal_minute > 55):
                if (marca_temporal_second is None):
                    return u'Mama'
                if (marca_temporal_second > 33):
                    return u'Piel'
                if (marca_temporal_second <= 33):
                    if (peso > 66):
                        return u'Mama'
                    if (peso <= 66):
                        return u'Cuello'
            if (marca_temporal_minute <= 55):
                if (_cuantos_familiares_ is None):
                    return u'Mama'
                if (_cuantos_familiares_ == u'2'):
                    if (peso > 78):
                        if (peso > 87):
                            return u'Huesos'
                        if (peso <= 87):
                            return u'H\xedgado'
                    if (peso <= 78):
                        if (marca_temporal_minute > 6):
                            return u'Mama'
                        if (marca_temporal_minute <= 6):
                            return u'Leucemia'
                if (_cuantos_familiares_ != u'2'):
                    if (edad is None):
                        return u'Mama'
                    if (edad > 32):
                        if (peso > 63):
                            return u'Cuello uterino'
                        if (peso <= 63):
                            if (peso > 62):
                                return u'Pr\xf3stata'
                            if (peso <= 62):
                                return u'Mama'
                    if (edad <= 32):
                        if (marca_temporal_second is None):
                            return u'Mama'
                        if (marca_temporal_second > 34):
                            if (edad > 22):
                                return u'Leucemia'
                            if (edad <= 22):
                                if (marca_temporal_second > 54):
                                    return u'Mama'
                                if (marca_temporal_second <= 54):
                                    if (estatura is None):
                                        return u'Leucemia'
                                    if (estatura > 174):
                                        return u'Mama'
                                    if (estatura <= 174):
                                        return u'Leucemia'
                        if (marca_temporal_second <= 34):
                            if (marca_temporal_second > 18):
                                return u'Mama'
                            if (marca_temporal_second <= 18):
                                if (marca_temporal_second > 12):
                                    if (peso > 71):
                                        if (peso > 78):
                                            return u'Pr\xf3stata'
                                        if (peso <= 78):
                                            return u'Cuello uterino'
                                    if (peso <= 71):
                                        return u'Leucemia'
                                if (marca_temporal_second <= 12):
                                    if (marca_temporal_second > 2):
                                        if (peso > 63):
                                            return u'Mama'
                                        if (peso <= 63):
                                            if (estatura is None):
                                                return u'Mama'
                                            if (estatura > 160):
                                                return u'Leucemia'
                                            if (estatura <= 160):
                                                return u'Mama'
                                    if (marca_temporal_second <= 2):
                                        return u'Leucemia'
        if (peso <= 60):
            if (_cuantos_familiares_ is None):
                return u'Mama'
            if (_cuantos_familiares_ == u'1'):
                if (marca_temporal_minute is None):
                    return u'Mama'
                if (marca_temporal_minute > 41):
                    if (marca_temporal_hour > 15):
                        return u'Huesos'
                    if (marca_temporal_hour <= 15):
                        return u'Mama'
                if (marca_temporal_minute <= 41):
                    return u'Mama'
            if (_cuantos_familiares_ != u'1'):
                if (marca_temporal_minute is None):
                    return u'Mama'
                if (marca_temporal_minute > 22):
                    if (estatura is None):
                        return u'Mama'
                    if (estatura > 157):
                        if (marca_temporal_second is None):
                            return u'Mama'
                        if (marca_temporal_second > 11):
                            if (marca_temporal_minute > 56):
                                return u'Leucemia'
                            if (marca_temporal_minute <= 56):
                                if (_has_tenido_algun_familiar_con_cancer_ is None):
                                    return u'Mama'
                                if (_has_tenido_algun_familiar_con_cancer_ == u'S\xed'):
                                    return u'Mama'
                                if (_has_tenido_algun_familiar_con_cancer_ == u'No'):
                                    if (peso > 57):
                                        return u'Mama'
                                    if (peso <= 57):
                                        return u'Cuello uterino'
                        if (marca_temporal_second <= 11):
                            if (estatura > 166.5):
                                return u'Cuello uterino'
                            if (estatura <= 166.5):
                                return u'Leucemia'
                    if (estatura <= 157):
                        if (marca_temporal_minute > 46):
                            return u'Pulm\xf3n'
                        if (marca_temporal_minute <= 46):
                            if (peso > 50):
                                return u'Cuello uterino'
                            if (peso <= 50):
                                return u'Leucemia'
                if (marca_temporal_minute <= 22):
                    if (marca_temporal_hour > 15):
                        if (peso > 49):
                            if (estatura is None):
                                return u'Pulm\xf3n'
                            if (estatura > 170.5):
                                return u'Mama'
                            if (estatura <= 170.5):
                                return u'Pulm\xf3n'
                        if (peso <= 49):
                            return u'Mama'
                    if (marca_temporal_hour <= 15):
                        if (marca_temporal_second is None):
                            return u'Mama'
                        if (marca_temporal_second > 14):
                            return u'Mama'
                        if (marca_temporal_second <= 14):
                            if (peso > 56):
                                return u'Mama'
                            if (peso <= 56):
                                return u'Leucemia'
    if (marca_temporal_hour <= 14):
        if (sexo is None):
            return u'Mama'
        if (sexo == u'Mujer'):
            if (edad is None):
                return u'Mama'
            if (edad > 43):
                return u'Cuello uterino'
            if (edad <= 43):
                if (_cuantos_familiares_ is None):
                    return u'Mama'
                if (_cuantos_familiares_ == u'2'):
                    if (peso is None):
                        return u'Mama'
                    if (peso > 46):
                        if (peso > 73):
                            return u'Mama'
                        if (peso <= 73):
                            return u'Est\xf3mago'
                    if (peso <= 46):
                        return u'Mama'
                if (_cuantos_familiares_ != u'2'):
                    if (marca_temporal_second is None):
                        return u'Mama'
                    if (marca_temporal_second > 42):
                        if (peso is None):
                            return u'Mama'
                        if (peso > 56):
                            if (marca_temporal_second > 55):
                                return u'Mama'
                            if (marca_temporal_second <= 55):
                                return u'Pr\xf3stata'
                        if (peso <= 56):
                            return u'Mama'
                    if (marca_temporal_second <= 42):
                        if (estatura is None):
                            return u'Mama'
                        if (estatura > 157.5):
                            return u'Mama'
                        if (estatura <= 157.5):
                            if (edad > 18):
                                return u'Mama'
                            if (edad <= 18):
                                return u'Pulm\xf3n'
        if (sexo == u'Hombre'):
            if (marca_temporal_minute is None):
                return u'Pulm\xf3n'
            if (marca_temporal_minute > 51):
                if (peso is None):
                    return u'Mama'
                if (peso > 66):
                    return u'Mama'
                if (peso <= 66):
                    return u'Huesos'
            if (marca_temporal_minute <= 51):
                if (_cuantos_familiares_ is None):
                    return u'Pulm\xf3n'
                if (_cuantos_familiares_ == u'1'):
                    return u'Pulm\xf3n'
                if (_cuantos_familiares_ != u'1'):
                    if (peso is None):
                        return u'Piel'
                    if (peso > 69):
                        return u'Piel'
                    if (peso <= 69):
                        return u'Pulm\xf3n'
