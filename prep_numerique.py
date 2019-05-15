__author__ = '3Points'
import ftplib
import os
import sys
import crypt
import random
import shutil

print('------------------------')
print('- Debut du traitement! -')
print('------------------------')
def salt():
    """Returns a string of 2 random letters"""
    letters = 'abcdefghijklmnopqrstuvwxyz' \
              'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
              '0123456789/.'
    return random.choice(letters) + random.choice(letters)

#print('Number of arguments:', len(sys.argv))
code_utilisateur=str(sys.argv[1])
print('Code utilisateur = [' + code_utilisateur + ']')

mot_passe=str(sys.argv[2])
print('Mot de passe = [' + mot_passe + ']')

photo_joueur = str(sys.argv[3])
print('Photo joueur = [' + photo_joueur + ']')

photo_equipe = str(sys.argv[4])
print('Photo equipe = [' + photo_equipe + ']')

transfert_ftp = str(sys.argv[5])
print('Transfert FTP = [' + transfert_ftp + ']')

# Je dois faire la structure de répertoire sur le Raspberry Pi et faire l'envoi complet vers le site IMAGME.COM par la suite.
dir_transfert = '/home/pi/IMAGME_Transferts/'
dir_photos = '/home/pi/IMAGME_Photos/'
#dir_transfert = '/Users/gilo/Documents/IMAGME/test_destination/'
#dir_photos = '/Users/gilo/Documents/IMAGME/test_source/'


if not os.path.exists(dir_transfert + code_utilisateur):
    os.makedirs(dir_transfert + code_utilisateur)    
        
    shutil.copy2(dir_photos + photo_joueur, dir_transfert + code_utilisateur + '/' + photo_joueur)
    shutil.copy2(dir_photos + photo_equipe, dir_transfert + code_utilisateur + '/' + photo_equipe)
    
    #os.system('convert ' + dir_transfert + code_utilisateur + '/' + photo_joueur + ' -resize 200x200 ' + dir_transfert + code_utilisateur + '/thumbnail_' + photo_joueur)
    #os.system('convert ' + dir_transfert + code_utilisateur + '/' + photo_equipe + ' -resize 200x200 ' + dir_transfert + code_utilisateur + '/thumbnail_' + photo_equipe)


if not os.path.exists(dir_transfert + code_utilisateur + '/.htaccess'):
    fichier_htaccess = open(dir_transfert + code_utilisateur + '/.htaccess', 'w')
    fichier_htaccess.write("AuthType Basic\n")
    fichier_htaccess.write("AuthName \"Authorisation requise\"\n")
    fichier_htaccess.write("AuthUserFile /home/content/60/11707360/html/photos_numeriques/" + code_utilisateur + "/.htpasswd\n")
    fichier_htaccess.write("require valid-user\n")
    fichier_htaccess.close()

if not os.path.exists(dir_transfert + code_utilisateur + '/.htpasswd'):
    fichier_htpasswd = open(dir_transfert + code_utilisateur + '/.htpasswd', 'w')
    fichier_htpasswd.write(code_utilisateur + ':' + crypt.crypt(mot_passe,salt()))
    fichier_htpasswd.close()

if not os.path.exists(dir_transfert + code_utilisateur + '/index.html'):
    fichier_index = open(dir_transfert + code_utilisateur + '/index.html', 'w')
    fichier_index.write("<!doctype html>\n")
    fichier_index.write("<html>\n")
    fichier_index.write("  <head>\n")
    fichier_index.write("    <style>\n")
    fichier_index.write("      #rcorners {\n")
    fichier_index.write("        border-radius: 25px;\n")
    fichier_index.write("        border: 2px solid #73AD21;\n")
    fichier_index.write("        padding: 10px;\n") 
    fichier_index.write("        width: 150px;\n")
    fichier_index.write("        height: 120px;\n")
    fichier_index.write("        z-index: -1;\n")
    fichier_index.write("      }\n")

    fichier_index.write("      #rcorners2 {\n")
    fichier_index.write("        position: absolute;\n")
    fichier_index.write("        left: 190px;\n")
    fichier_index.write("        top: 95px;\n")
    fichier_index.write("        border-radius: 25px;\n")
    fichier_index.write("        border: 2px solid #73AD21;\n")
    fichier_index.write("        padding: 10px;\n") 
    fichier_index.write("        width: 150px;\n")
    fichier_index.write("        height: 120px;\n")
    fichier_index.write("        z-index: -1;\n")
    fichier_index.write("      }\n")

    fichier_index.write("      #rcorners3 {\n")
    fichier_index.write("        position: absolute;\n")
    fichier_index.write("        left: 372px;\n")
    fichier_index.write("        top: 95px;\n")
    fichier_index.write("        border-radius: 25px;\n")
    fichier_index.write("        border: 2px solid #73AD21;\n")
    fichier_index.write("        padding: 10px;\n")
    fichier_index.write("        width: 150px;\n")
    fichier_index.write("        height: 120px;\n")
    fichier_index.write("        z-index: 9;\n")
    fichier_index.write("      }\n")

    fichier_index.write("      #check {\n")
    fichier_index.write("        position: absolute;\n")
    fichier_index.write("        left: 55px;\n")
    fichier_index.write("        top: 215px;\n")
    fichier_index.write("        background: url(../check.png) 0 0;\n")
    fichier_index.write("      }\n")

    fichier_index.write("      #check2 {\n")
    fichier_index.write("        position: absolute;\n")
    fichier_index.write("        left: 240px;\n")
    fichier_index.write("        top: 215px;\n")
    fichier_index.write("        background: url(../check.png) 0 0;\n")
    fichier_index.write("      }\n")

    fichier_index.write("      input{\n")
    fichier_index.write("        -webkit-border-radius: 5px; //For Safari, etc.\n")
    fichier_index.write("        -moz-border-radius: 5px; //For Mozilla, etc.\n")
    fichier_index.write("        border-radius: 5px; //CSS3 Feature\n")
    fichier_index.write("      }\n")

    fichier_index.write("    </style>\n")
    fichier_index.write("  </head>\n")
    fichier_index.write("  <body>\n")
    fichier_index.write("    <h1>R&eacute;cup&eacute;ration de vos photographies</h1>\n")

    fichier_index.write("    <table border='0' cellpadding='0' cellspacing='0'>\n")
    fichier_index.write("      <tbody>\n")
    fichier_index.write("        <tr>\n")
    fichier_index.write("          <td>\n")
    fichier_index.write("            <p id='rcorners' valign='center'>\n")
    fichier_index.write("              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Connectez-Vous<br><br>www.imagme.com/login\n")
    fichier_index.write("            </p>\n")
    fichier_index.write("          </td>\n")
    fichier_index.write("          <td>\n")
    fichier_index.write("            <p id='rcorners2' valign='center'>\n")
    fichier_index.write("              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identifiez-Vous<br><br><br><br>\n")
    fichier_index.write("              <form action='index.html'>\n")
    fichier_index.write("                <br><br><br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code usager:&nbsp;\n")
    fichier_index.write("                <input type='text' name='code' size='7' readonly><br>\n")
    fichier_index.write("                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mot de passe:\n")
    fichier_index.write("                <input type='text' name='password' size='7' readonly>\n")
    fichier_index.write("                <br><br><br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n")
    fichier_index.write("              </form>\n")
    fichier_index.write("            </p>\n")
    fichier_index.write("          </td>\n")
    fichier_index.write("          <td>\n")
    fichier_index.write("            <p id='rcorners3' valign='center'>\n")
    fichier_index.write("              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T&eacute;l&eacute;charger<br><br>\n")
    fichier_index.write("		       <a href=\"" + photo_joueur + "\">Photo Joueur</a>\n")
    fichier_index.write("		       <BR>\n")
    fichier_index.write("		       <a href=\"" + photo_equipe + "\">Photo &Eacute;quipe</a>\n")
    fichier_index.write("            </p>\n")
    fichier_index.write("          </td>\n")
    fichier_index.write("        </tr>\n")
    fichier_index.write("      </tbody>\n")
    fichier_index.write("    </table>\n")
    fichier_index.write("    <img id='check' src='../transparent.png' width='75'>\n")
    fichier_index.write("    <img id='check2' src='../transparent.png' width='75'>\n")

    fichier_index.write("  </body>\n")
    fichier_index.write("</html>\n")
    fichier_index.close()

if transfert_ftp == '1':
    print('\n\nFTP start')
    repertoire_imagme_global = '/photos_numeriques/'

    session = ftplib.FTP('www.imagme.com','godimagme','Kil01m@r')

    for root, dirs, files in os.walk(dir_transfert, topdown=False):
        print('------------------------------------------------------')
        repertoire_raspberry = os.path.basename(root)

        if not repertoire_raspberry == '':
             try:
                session.mkd(repertoire_imagme_global + repertoire_raspberry)
                print('\nCreation repertoire: ' + '[www.imagme.com] ' + repertoire_imagme_global + repertoire_raspberry)

             except ftplib.error_perm:
                pass

        for f in files:
            print('Transfert: ' + root + '/' + f + ' -> ' + '[www.imagme.com] ' + repertoire_imagme_global + repertoire_raspberry + '/' + f)
            session.storbinary('STOR ' + repertoire_imagme_global + repertoire_raspberry + '/' + f, open(root + '/' + f, 'rb'))

    session.quit()
    print('\nFTP stop')

print('----------------------')
print('- Fin de traitement! -')
print('----------------------')