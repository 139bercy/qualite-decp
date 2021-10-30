class General:
    def __init__(self, valeur, rang):
        self.valeur = valeur
        self.rang = rang

    def to_dict(self):
        return {"valeur": self.valeur, "rang": self.rang}

    @classmethod
    def from_dict(cls, d):
        valeur = d["valeur"]
        rang = d["rang"]
        return cls(valeur, rang)


class Coherence:
    def __init__(
        self,
        valeur: float,
        rang: int,
        incoherences_temporelles,
        incoherences_montant_duree,
    ):
        self.valeur = valeur
        self.rang = rang
        self.incoherences_temporelles = incoherences_temporelles
        self.incoherences_montant_duree = incoherences_montant_duree

    def to_dict(self):
        return {
            "synthese": {"valeur": self.valeur, "rang": self.rang},
            "detail": {
                "incoherences_temporelles": self.incoherences_temporelles,
                "incoherences_montant_duree": self.incoherences_montant_duree,
            },
        }

    @classmethod
    def from_dict(cls, d):
        valeur = d["synthese"]["valeur"]
        rang = d["synthese"]["rang"]
        incoherences_temporelles = d["detail"]["incoherences_temporelles"]
        incoherences_montant_duree = d["detail"]["incoherences_montant_duree"]
        return cls(valeur, rang, incoherences_temporelles, incoherences_montant_duree)


class Exactitude:
    def __init__(self, valeur: float, rang: int, valeurs_aberrantes, valeurs_extremes):
        self.valeur = valeur
        self.rang = rang
        self.valeurs_aberrantes = valeurs_aberrantes
        self.valeurs_extremes = valeurs_extremes

    def to_dict(self):
        return {
            "synthese": {"valeur": self.valeur, "rang": self.rang},
            "detail": {
                "valeurs_aberrantes": self.valeurs_aberrantes,
                "valeurs_extremes": self.valeurs_extremes,
            },
        }

    @classmethod
    def from_dict(cls, d):
        valeur = d["synthese"]["valeur"]
        rang = d["synthese"]["rang"]
        valeurs_aberrantes = d["detail"]["valeurs_aberrantes"]
        valeurs_extremes = d["detail"]["valeurs_extremes"]
        return cls(valeur, rang, valeurs_aberrantes, valeurs_extremes)


class Validite:
    def __init__(
        self,
        valeur: float,
        rang: int,
        jours_moyens_depuis_derniere_publication: float,
        depassements_delai_entre_notification_et_publication: float,
    ):
        self.valeur = valeur
        self.rang = rang
        self.jours_moyens_depuis_derniere_publication = (
            jours_moyens_depuis_derniere_publication
        )
        self.depassements_delai_entre_notification_et_publication = (
            depassements_delai_entre_notification_et_publication
        )

    def to_dict(self):
        return {
            "synthese": {"valeur": self.valeur, "rang": self.rang},
            "detail": {
                "jours_moyens_depuis_derniere_publication": self.jours_moyens_depuis_derniere_publication,
                "depassements_delai_entre_notification_et_publication": self.depassements_delai_entre_notification_et_publication,
            },
        }

    @classmethod
    def from_dict(cls, d):
        valeur = d["synthese"]["valeur"]
        rang = d["synthese"]["rang"]
        jours_moyens_depuis_derniere_publication = d["detail"][
            "jours_moyens_depuis_derniere_publication"
        ]
        depassements_delai_entre_notification_et_publication = d["detail"][
            "depassements_delai_entre_notification_et_publication"
        ]
        return cls(
            valeur,
            rang,
            jours_moyens_depuis_derniere_publication,
            depassements_delai_entre_notification_et_publication,
        )


class Completude:
    def __init__(
        self, valeur: float, rang: int, donnees_manquantes, valeurs_non_renseignees
    ):
        self.valeur = valeur
        self.rang = rang
        self.donnees_manquantes = donnees_manquantes
        self.valeurs_non_renseignees = valeurs_non_renseignees

    def to_dict(self):
        return {
            "synthese": {"valeur": self.valeur, "rang": self.rang},
            "detail": {
                "donnees_manquantes": self.donnees_manquantes,
                "valeurs_non_renseignees": self.valeurs_non_renseignees,
            },
        }

    @classmethod
    def from_dict(cls, d):
        valeur = d["synthese"]["valeur"]
        rang = d["synthese"]["rang"]
        donnees_manquantes = d["detail"]["donnees_manquantes"]
        valeurs_non_renseignees = d["detail"]["valeurs_non_renseignees"]
        return cls(valeur, rang, donnees_manquantes, valeurs_non_renseignees)


class Conformite:
    def __init__(
        self,
        valeur: float,
        rang: int,
        caracteres_mal_encodes,
        formats_non_valides,
        valeurs_non_valides,
    ):
        self.valeur = valeur
        self.rang = rang
        self.caracteres_mal_encodes = caracteres_mal_encodes
        self.formats_non_valides = formats_non_valides
        self.valeurs_non_valides = valeurs_non_valides

    def to_dict(self):
        return {
            "synthese": {"valeur": self.valeur, "rang": self.rang},
            "detail": {
                "caracteres_mal_encodes": self.caracteres_mal_encodes,
                "formats_non_valides": self.formats_non_valides,
                "valeurs_non_valides": self.valeurs_non_valides,
            },
        }

    @classmethod
    def from_dict(cls, d):
        valeur = d["synthese"]["valeur"]
        rang = d["synthese"]["rang"]
        caracteres_mal_encodes = d["detail"]["caracteres_mal_encodes"]
        formats_non_valides = d["detail"]["formats_non_valides"]
        valeurs_non_valides = d["detail"]["valeurs_non_valides"]
        return cls(
            valeur,
            rang,
            caracteres_mal_encodes,
            formats_non_valides,
            valeurs_non_valides,
        )


class Singularite:
    def __init__(
        self, valeur: float, rang: int, identifiants_non_uniques, lignes_dupliquees
    ):
        self.valeur = valeur
        self.rang = rang
        self.identifiants_non_uniques = identifiants_non_uniques
        self.lignes_dupliquees = lignes_dupliquees

    def to_dict(self):
        return {
            "synthese": {"valeur": self.valeur, "rang": self.rang},
            "detail": {
                "identifiants_non_uniques": self.identifiants_non_uniques,
                "lignes_dupliquees": self.lignes_dupliquees,
            },
        }

    @classmethod
    def from_dict(cls, d):
        valeur = d["synthese"]["valeur"]
        rang = d["synthese"]["rang"]
        identifiants_non_uniques = d["detail"]["identifiants_non_uniques"]
        lignes_dupliquees = d["detail"]["lignes_dupliquees"]
        return cls(valeur, rang, identifiants_non_uniques, lignes_dupliquees)