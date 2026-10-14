Source: https://no-sleep-pika.online/guide/fr/ai-overnight-electricity-cost/
Language: fr

MAC GUIDE · 2026-10-15

# Quand l’IA travaille la nuit, qui paie l’électricité ?

Estimons huit heures de travail avec des hypothèses explicites, en séparant électricité domestique et frais du service d’IA.

## Deux dépenses distinctes

Avec l’IA dans le cloud, le fournisseur effectue le calcul principal du modèle. Votre Mac consomme encore pour les compilations et tests locaux. Avec un modèle local, il effectue aussi le calcul du modèle. Abonnement ou API et électricité sont deux dépenses différentes ; une mesure à la prise ne comprend pas le centre de données.

## Le coût de huit heures

Énergie : puissance moyenne en W × heures ÷ 1 000. Multipliez les kWh par votre tarif. Exemple hypothétique : huit heures par jour, trente jours, 0,20 USD/kWh. À 10W : 0,08kWh et 0,016 USD par nuit, puis 2,4kWh et 0,48 USD sur trente nuits. À 30W : 0,24kWh et 0,048 USD, puis 7,2kWh et 1,44 USD. À 60W : 0,48kWh et 0,096 USD, puis 14,4kWh et 2,88 USD.

Ce ne sont ni des mesures de MacBook ni un tarif local. Taxes et tranches peuvent modifier la facture. Pour le surcoût par rapport à la veille, mesurez puis soustrayez la consommation en veille sur la même durée.

## La puissance du chargeur ne suffit pas

Un chargeur de 70W ne signifie pas une consommation constante de 70W. Batterie, écrans et tâches locales modifient la demande. Éteindre l’écran peut réduire son énergie, sans économie identique pour tous les Mac.

## Mesurer sa propre tâche

Utilisez un wattmètre de prise mesurant les kWh cumulés, selon sa notice. 0,06kWh en deux heures correspond à 30W moyens. Cela donne 0,24kWh sur huit heures uniquement à charge comparable. Mesurez de préférence toute la tâche, notez les niveaux de batterie et excluez explicitement les écrans alimentés séparément.

## pika économise-t-il l’énergie ?

pika maintient les tâches que la veille pourrait interrompre. Il ne mesure pas l’électricité et ne réduit pas les frais d’IA. Garder le Mac éveillé peut augmenter sa consommation. Vérifiez le service auxiliaire, activez Session, laissez Monitor désactivé si l’écran n’est pas nécessaire, puis testez brièvement le couvercle fermé. Désactivez Session à la fin. Les demandes d’autorisation et erreurs réseau restent à traiter séparément.

[Télécharger pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [Aide à l’installation](https://no-sleep-pika.online/install/)

## Avant de partir

Définissez le résultat attendu et la manière d’arrêter. Configurez limites ou alertes si disponibles ; ne comptez pas deux fois un abonnement existant comme dépense supplémentaire. Branchez le Mac sur une table ferme et ventilée, jamais dans un sac ou sous la literie.

Hypothèses et sources

Article du créateur de pika. Calcul : Virginia Cooperative Extension. Ventilation : Apple. Puissances et tarif en USD sont hypothétiques.

- [Virginia Cooperative Extension · Estimating appliance energy use](https://ext.vt.edu/content/pubs_ext_vt_edu/en/2901/2901-9014/2901-9014.html)

- [Apple · Mac operating temperatures](https://support.apple.com/en-us/102336)

Rédigé par le créateur de no-sleep-pika ; présente notre app.

[Télécharger pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Empêcher un Mac de se mettre en veille : écran fermé, caffeinate et pika →](https://no-sleep-pika.online/guide/fr/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/fr/ai-overnight-electricity-cost/index.md)
