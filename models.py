from django.db import models

from Agents.models import Classes


class Etudiants(models.Model):
    etudiant_code = models.CharField(primary_key=True, max_length=10)
    etudiant_matr = models.IntegerField(blank=True, null=True)
    etudiant_nom = models.CharField(max_length=100, blank=True, null=True)
    etudiant_pren = models.CharField(max_length=100, blank=True, null=True)
    etudiant_sexe = models.CharField(max_length=1, blank=True, null=True)
    etudiant_datn = models.DateTimeField(blank=True, null=True)
    etudiant_lieu = models.CharField(max_length=100, blank=True, null=True)
    etudiant_nati = models.CharField(max_length=75, blank=True, null=True)
    etudiant_phot = models.ImageField(blank=True, null=True)
    etudiant_adre = models.CharField(max_length=255, blank=True, null=True)
    etudiant_bpos = models.IntegerField(blank=True, null=True)
    etudiant_ville = models.CharField(max_length=75, blank=True, null=True)
    etudiant_pays = models.CharField(max_length=75, blank=True, null=True)
    etudiant_etat = models.CharField(max_length=15, blank=True, null=True)
    etudiant_crat = models.DateTimeField(blank=True, null=True)
    etudiant_upat = models.DateTimeField(blank=True, null=True)
    etudiant_enre = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'etudiants'


class Responsables(models.Model):
    responsable_code = models.CharField(primary_key=True, max_length=10)
    responsable_titre = models.CharField(max_length=5, blank=True, null=True)
    responsable_nom = models.CharField(max_length=100, blank=True, null=True)
    responsable_pren = models.CharField(max_length=100, blank=True, null=True)
    responsable_prof = models.CharField(max_length=75, blank=True, null=True)
    responsable_tel1 = models.CharField(max_length=22, blank=True, null=True)
    responsable_tel2 = models.TextField(blank=True, null=True)
    responsable_tel3 = models.CharField(max_length=22, blank=True, null=True)
    responsable_esms = models.BooleanField()
    responsable_legal = models.BooleanField()
    responsable_nsms = models.CharField(max_length=22, blank=True, null=True)
    responsable_adre = models.CharField(max_length=155, blank=True, null=True)
    responsable_pays = models.CharField(max_length=75, blank=True, null=True)
    responsable_ville = models.CharField(max_length=50, blank=True, null=True)
    responsable_boite = models.IntegerField(blank=True, null=True)
    responsable_mail = models.CharField(max_length=155, blank=True, null=True)
    responsable_crat = models.DateTimeField(blank=True, null=True)
    responsable_upat = models.DateTimeField(blank=True, null=True)
    responsable_enre = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'responsables'


class Tuteur(models.Model):
    responsable_code = models.OneToOneField(Responsables, models.DO_NOTHING, db_column='responsable_code', primary_key=True)  # The composite primary key (responsable_code, etudiant_code) found, that is not supported. The first column is selected.
    etudiant_code = models.ForeignKey(Etudiants, models.DO_NOTHING, db_column='etudiant_code')
    tuteur_annee = models.CharField(max_length=10, blank=True, null=True)
    tuteur_lienp = models.CharField(max_length=15, blank=True, null=True)
    tuteur_obsr = models.CharField(max_length=255, blank=True, null=True)
    tuteur_crat = models.DateTimeField(blank=True, null=True)
    tuteur_upat = models.DateTimeField(blank=True, null=True)
    tuteur_enre = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tuteur'
        unique_together = (('responsable_code', 'etudiant_code'),)

class Decisions(models.Model):
    decision_code = models.CharField(primary_key=True, max_length=10)
    etudiant_code = models.ForeignKey(Etudiants, models.DO_NOTHING, db_column='etudiant_code', blank=True, null=True)
    decision_type = models.CharField(max_length=25, blank=True, null=True)
    decision_date = models.DateTimeField(blank=True, null=True)
    decision_nume = models.CharField(max_length=6, blank=True, null=True)
    decision_annee = models.CharField(max_length=10, blank=True, null=True)
    decision_prio = models.CharField(max_length=35, blank=True, null=True)
    decision_dscr = models.TextField(blank=True, null=True)
    decision_motif = models.TextField(blank=True, null=True)
    decision_etat = models.CharField(max_length=60, blank=True, null=True)
    decision_file = models.CharField(max_length=10, blank=True, null=True)
    decision_crat = models.DateTimeField(blank=True, null=True)
    decision_upat = models.DateTimeField(blank=True, null=True)
    decision_enre = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'decisions'


class Documents(models.Model):
    document_code = models.CharField(primary_key=True, max_length=10)
    etudiant_code = models.ForeignKey(Etudiants, models.DO_NOTHING, db_column='etudiant_code', blank=True, null=True)
    document_type = models.CharField(max_length=15, blank=True, null=True)
    document_date = models.DateTimeField(blank=True, null=True)
    document_num = models.CharField(max_length=15, blank=True, null=True)
    document_nom = models.CharField(max_length=50, blank=True, null=True)
    document_desc = models.TextField(blank=True, null=True)
    document_file = models.CharField(max_length=10, blank=True, null=True)
    document_crat = models.DateTimeField(blank=True, null=True)
    document_upat = models.DateTimeField(blank=True, null=True)
    document_enre = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'documents'

class Inscriptions(models.Model):
    classe_code = models.OneToOneField(Classes, models.DO_NOTHING, db_column='classe_code', primary_key=True)  # The composite primary key (classe_code, etudiant_code, inscription_annee) found, that is not supported. The first column is selected.
    etudiant_code = models.ForeignKey(Etudiants, models.DO_NOTHING, db_column='etudiant_code')
    inscription_annee = models.CharField(max_length=10)
    inscription_stat = models.CharField(max_length=35, blank=True, null=True)
    inscription_date = models.DateTimeField(blank=True, null=True)
    inscription_allo = models.BooleanField()
    inscription_disp = models.BooleanField()
    inscription_ddsp = models.DateTimeField(blank=True, null=True)
    inscription_mdsp = models.CharField(max_length=255, blank=True, null=True)
    inscription_my1s = models.FloatField(blank=True, null=True)
    inscription_my2s = models.FloatField(blank=True, null=True)
    inscription_dcsn = models.CharField(max_length=35, blank=True, null=True)
    inscription_obsr = models.CharField(max_length=255, blank=True, null=True)
    inscription_crat = models.DateTimeField(blank=True, null=True)
    inscription_upat = models.DateTimeField(blank=True, null=True)
    inscription_enre = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'inscriptions'
        unique_together = (('classe_code', 'etudiant_code', 'inscription_annee'),)

