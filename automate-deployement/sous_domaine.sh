#!/bin/bash

echo "$SOUS_DOMAINE  IN  CNAME  @" >> /etc/bind/db.iteams.mg
rndc reload
