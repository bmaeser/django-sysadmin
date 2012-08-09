from django.db import models

class VirtualMailboxDomain(models.Model):
    """
    Model to handle virtual_mailbox_domains in 

    see: http://www.postfix.org/postconf.5.html#virtual_mailbox_domains
    """
    ## domain to listen to
    ## domain must not be included in virtual_alias_domains
    domain = models.CharField(max_length=255, unique=True, db_index=True)
    comment = models.CharField(max_length=255, null=True, blank=True)

    active = models.BooleanField(default=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'virtual_mailbox_domains'
        verbose_name = "virtual mailbox domain"

class VirtualMailboxMaps(models.Model):
    """
    Model to handle virtual_mailbox_maps in postfix

    see: http://www.postfix.org/postconf.5.html#virtual_mailbox_maps
    """
    ## 'from' emailadress
    ## note: domain musst be in virtual_mailbox_domains !OR! 
    ## virtual_alias_domains
    mailbox = models.CharField(max_length=255, db_index=True)
    domain = models.CharField(max_length=255, db_index=True)
    ## comma-separated list of target email-adresses
    maildir = models.CharField(max_length=255, unique=True)
    comment = models.CharField(max_length=255, null=True, blank=True)

    active = models.BooleanField(default=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'virtual_mailboxes'
        verbose_name = "virtual mailbox"
        verbose_name_plural = "virtual mailboxes"
        unique_together = ("mailbox", "domain")


class VirtualAliasMaps(models.Model):
    """
    Model to handle virtual_alias_maps in postfix

    see: http://www.postfix.org/postconf.5.html#virtual_alias_maps
    """
    ## 'from' emailadress
    ## note: domain musst be in virtual_mailbox_domains !OR! 
    ## virtual_alias_domains
    alias = models.CharField(max_length=255, unique=True, db_index=True)
    ## comma-separated list of target email-adresses
    goto = models.CharField(max_length=255)
    comment = models.CharField(max_length=255, null=True, blank=True)

    active = models.BooleanField(default=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'virtual_aliases'
        verbose_name = "virtual alias"
        verbose_name_plural = "virtual aliases"


class Sasl2Auth(models.Model):
    """
    Model to handle user:pass accounts in sasl2-auxprop-sql
    this is usefull, if you have apps or other mtas that want to 
    relay email through this postfix-server

    see: http://www.postfix.org/SASL_README.html#auxprop_sql
    """

    username = models.CharField(max_length=255, unique=True, db_index=True)
    password = models.CharField(max_length=255, db_index=True)
    comment = models.CharField(max_length=255, null=True, blank=True)

    active = models.BooleanField(default=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'relay_users'
        verbose_name = "relay user"