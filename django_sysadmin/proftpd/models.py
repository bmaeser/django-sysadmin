from django.db import models


class FTPUser(models.Model):
    """
    Model to handle FTP-Users

    see: http://www.proftpd.org/docs/directives/linked/config_ref_SQLAuthTypes.html
    and: http://www.proftpd.org/docs/directives/linked/config_ref_SQLUserInfo.html
    """

    username = models.CharField(max_length=255, unique=True, db_index=True)
    password = models.CharField(max_length=255, db_index=True)

    ## unix user info
    uid = models.IntegerField()
    gid = models.IntegerField()

    homedir = models.CharField(max_length=255)
    shell = models.CharField(max_length=255)

    #optional comment
    comment = models.CharField(max_length=255, null=True, blank=True)

    active = models.BooleanField(default=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ftp_users'
        verbose_name = 'FTP user'


## possible todo: default uid/guid/homedir/shell in settings.py?