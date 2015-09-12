# -*- coding: utf-8 -*-
#
## ========================================================================== ##
##                                                                            ##
##     FICHERO DE EXPRESIONES REGULARES PARA SU UTILIZACIÓN CON PYWIKIBOT     ##
##                                                                            ##
## ========================================================================== ##
#
#   Copyright (C) 2012-2015, David Abián <da [at] davidabian.com>
#
#   This program is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the Free
#   Software Foundation, either version 3 of the License, or (at your option)
#   any later version.
#
#   This program is distributed in the hope that it will be useful, but WITHOUT
#   ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#   FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#   more details.
#
#   You should have received a copy of the GNU General Public License along with
#   this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ============================================================================ #



# ============================================================================ #
#
#   +-------------------------+  https://es.wikipedia.org/wiki/User:Invadibot
#   |    Invadibot, global    |  https://meta.wikimedia.org/wiki/User:Invadibot
#   +-------------------------+  http://davidabian.com/invadibot/
#
#   [en] Fixing links to Wikimedia projects and applying protocol-relative URLs.
#   [es] Expresiones regulares para mejorar enlaces a proyectos Wikimedia y 
#        aplicar direcciones URL de protocolo relativo.
#
#   Goals and procedures:
#   <https://meta.wikimedia.org/wiki/User:Invadibot/scope/meta-2>
#
# <nowiki>
fixes['inva-wmp-prurls'] = {
    'dotall': False,
    'nocase': False,
    'recursive': True,
    'regex': True,
    'msg': {
        #
        #  Please add an edit summary for your project if not defined.
        #
        '_default': u'[[m:User:Invadibot/scope/meta-2|Bot]]:'
                    u' Fixing links to Wikimedia projects and applying'
                    u' protocol-relative URLs',

        'an':       u'[[m:User:Invadibot/scope/meta-2|Bot]]:'
                    u' Apanyando vinclos enta prochectos Wikimedia y'
                    u' aplicando adrezas URL de protocolo relativo',

        'en':       u'[[m:User:Invadibot/scope/meta-2|Bot]]:'
                    u' Fixing links to Wikimedia projects and applying'
                    u' protocol-relative URLs',

        'es':       u'[[m:User:Invadibot/scope/meta-2|Bot]]:'
                    u' Arreglando enlaces a proyectos Wikimedia y aplicando'
                    u' direcciones URL de protocolo relativo',

        'fa':       u'[[m:User:Invadibot/scope/meta-2|ربات]]: تصحیح پیوند به پروژه‌های خواهر و تبدیل کردن پیوندها به خنثی در برابر پروتکل', # --Ladsgroup

        'foundation': u'[[m:User:Invadibot/scope/meta-2|Bot]]:'
                      u' Fixing links to Wikimedia projects and applying'
                      u' protocol-relative URLs',

        'gl':       u'[[m:User:Invadibot/scope/meta-2|Bot]]:'
                    u' Arranxando ligazóns a proxectos Wikimedia e aplicando'
                    u' enderezos URL de protocolo relativo',

        'meta':     u'[[m:User:Invadibot/scope/meta-2|Bot]]:'
                    u' Fixing links to Wikimedia projects and applying'
                    u' protocol-relative URLs',

        'test':     u'[[m:User:Invadibot/scope/meta-2|Bot]]:'
                    u' Testing links to Wikimedia projects',

        'wmf':      u'[[m:User:Invadibot/scope/meta-2|Bot]]:'
                    u' Fixing links to Wikimedia projects and applying'
                    u' protocol-relative URLs',
    },
    'replacements': [
        (ur'\[http://([^@:/ ]+?\.)?wik(ipedia'
                                   ur'|inews'
                                   ur'|isource'
                                   ur'|ibooks'
                                   ur'|iquote'
                                   ur'|iversity'
                                   ur'|tionary'
                                   ur'|idata'
                                   ur'|ivoyage'
                                   ur'|imedia)\.org([^\.])', ur'[//\1wik\2.org\3'),
        (ur'\[http://(www\.)?mediawiki\.org',            ur'[//\1mediawiki.org'),
        (ur'\[http://(www\.)?wikimediafoundation\.org',  ur'[//\1wikimediafoundation.org'),
        (ur'\[http://(www\.)?tools\.wmflabs\.org',       ur'[//tools.wmflabs.org'),
        (ur'\[//(?:www\.)?mail\.wikipedia\.org',         ur'[//lists.wikimedia.org'),
        (ur'\[//(?:www\.)?([^@:/ (www)]+)\.wikipedia\.org/wiki/([^\s\]\?\|]+) (.+?)\]',   ur'[[w:\1:\2|\3]]'),
        (ur'\[//(?:www\.)?([^@:/ (www)]+)\.wikinews\.org/wiki/([^\s\]\?\|]+) (.+?)\]',    ur'[[n:\1:\2|\3]]'),
        (ur'\[//(?:www\.)?([^@:/ (www)]+)\.wikisource\.org/wiki/([^\s\]\?\|]+) (.+?)\]',  ur'[[s:\1:\2|\3]]'),
        (ur'\[//(?:www\.)?([^@:/ (www)]+)\.wikibooks\.org/wiki/([^\s\]\?\|]+) (.+?)\]',   ur'[[b:\1:\2|\3]]'),
        (ur'\[//(?:www\.)?([^@:/ (www)]+)\.wikiquote\.org/wiki/([^\s\]\?\|]+) (.+?)\]',   ur'[[q:\1:\2|\3]]'),
        (ur'\[//(?:www\.)?([^@:/ (www)]+)\.wikiversity\.org/wiki/([^\s\]\?\|]+) (.+?)\]', ur'[[v:\1:\2|\3]]'),
        (ur'\[//(?:www\.)?([^@:/ (www)]+)\.wiktionary\.org/wiki/([^\s\]\?\|]+) (.+?)\]',  ur'[[wikt:\1:\2|\3]]'),
        (ur'\[//(?:www\.)?([^@:/ (www)]+)\.wikivoyage\.org/wiki/([^\s\]\?\|]+) (.+?)\]',  ur'[[wikivoyage:\1:\2|\3]]'),
        (ur'\[//(?:www\.)?wikidata\.org/wiki/([^\s\]\?\|]+) (.+?)\]',                     ur'[[d:\1|\2]]'),
        (ur'\[//(?:www\.)?mediawiki\.org/wiki/([^\s\]\?\|]+) (.+?)\]',                    ur'[[mw:\1|\2]]'),
        (ur'\[//(?:www\.)?wikimediafoundation\.org/wiki/([^\s\]\?\|]+) (.+?)\]',          ur'[[wmf:\1|\2]]'),
        (ur'\[//(?:www\.)?meta\.wikimedia\.org/wiki/([^\s\]\?\|]+) (.+?)\]',              ur'[[m:\1|\2]]'),
        (ur'\[//(?:www\.)?outreach\.wikimedia\.org/wiki/([^\s\]\?\|]+) (.+?)\]',          ur'[[outreach:\1|\2]]'),
        (ur'\[//(?:www\.)?wikitech\.wikimedia\.org/wiki/([^\s\]\?\|]+) (.+?)\]',          ur'[[wikitech:\1|\2]]'),
        (ur'\[//(?:www\.)?commons\.wikimedia\.org/wiki/([^\s\]\?\|]+) (.+?)\]',           ur'[[c:\1|\2]]'),
        (ur'\[//tools\.wmflabs\.org/([^\s\]\?\|]+) (.+?)\]',                              ur'[[toollabs:\1|\2]]'),
        #
        #  One of the following lines can be uncommented and adjusted
        #  depending on the project in which this script is going to run.
        #
        #(ur'\[\[:?m:(.+?)\]\]',             ur'[[:\1]]'), # Meta-Wiki
        #(ur'\[\[:?d:(.+?)\]\]',             ur'[[:\1]]'), # Wikidata
        #(ur'\[\[:?mw:(.+?)\]\]',            ur'[[:\1]]'), # MediaWiki
        #(ur'\[\[:?outreach:(.+?)\]\]',      ur'[[:\1]]'), # Outreach
        #(ur'\[\[:?commons:(.+?)\]\]',       ur'[[:\1]]'), # Commons
        #(ur'\[\[:?wikitech:(.+?)\]\]',      ur'[[:\1]]'), # Wikitech
        #(ur'\[\[:?w:en:(.+?)\]\]',          ur'[[:\1]]'), # Wikipedia (replace "en" by the language code)
        #(ur'\[\[:?n:en:(.+?)\]\]',          ur'[[:\1]]'), # Wikinews (replace "en" by the language code)
        #(ur'\[\[:?s:en:(.+?)\]\]',          ur'[[:\1]]'), # Wikisource (replace "en" by the language code)
        #(ur'\[\[:?b:en:(.+?)\]\]',          ur'[[:\1]]'), # Wikibooks (replace "en" by the language code)
        #(ur'\[\[:?q:en:(.+?)\]\]',          ur'[[:\1]]'), # Wikiquote (replace "en" by the language code)
        #(ur'\[\[:?v:en:(.+?)\]\]',          ur'[[:\1]]'), # Wikiversity (replace "en" by the language code)
        #(ur'\[\[:?wikt:en:(.+?)\]\]',       ur'[[:\1]]'), # Wiktionary (replace "en" by the language code)
        #(ur'\[\[:?wikivoyage:en:(.+?)\]\]', ur'[[:\1]]'), # Wikivoyage (replace "en" by the language code)
        #(ur'\[\[:?(?:foundation|wikimedia|wmf):(.+?)\]\]', ur'[[:\1]]'), # Foundation Wiki
    ],
    'exceptions': {
        'title': [
            '\.(css|js|php|py|sh)',
            '([Bb]lack'
             '|[Gg]r[ae]y'
             '|[Ww]hite'
             ')'
             '[ _]?[Ll]ist',
            '([Ss]abliera'
             '|[Ss]and[ _]?('
              '[Bb]ox'
              '|[Pp]ut'
              '|[Cc]haschte'
              '|[Kk]assen?'
              '|[Kk]assinn'
              '|[Ll][aå]dan'
              ')'
             '|('
              '[Zz]ona'
              '|[Pp][aáà](g|ch)ina'
              ')[ _]?de[ _]?('
               '[Pp]r(ue[bv]as?'
               '|o[bv][ae]s'
               '|e[bv]atinas?'
               ')|[Tt]estes?'
              ')'
             ')',
            # for Persian, no need to make it very general --Ladsgroup
            u'(صفحه[ _]تمرین|گودال)',
        ],
        'inside': [
            (ur'\[//(www\.)?([^@:/ (www)]+)\.[a-z]+\.org/wiki/[^\s\]\?\|]+ (.*?\[\[.*?\]\].*?)+\]'),
            (ur'\[//[^\s\]]{400}.*?\]'),
            (ur'\[http://(www\.)?(apt'
                              ur'|bayes'
                              ur'|bayle'
                              ur'|brewster'
                              ur'|commons\.prototype'
                              ur'|commonsprototype\.tesla\.usability'
                              ur'|cs'
                              ur'|cz'
                              ur'|dataset2'
                              ur'|de\.prototype'
                              ur'|download'
                              ur'|dumps'
                              ur'|ekrem'
                              ur'|emery'
                              ur'|en\.prototype'
                              ur'|ersch'
                              ur'|etherpad'
                              ur'|fenari'
                              ur'|flaggedrevssandbox'
                              ur'|flgrevsandbox'
                              ur'|gallium|ganglia'
                              ur'|ganglia3'
                              ur'|harmon'
                              ur'|hume'
                              ur'|ipv4\.labs'
                              ur'|ipv6and4\.labs'
                              ur'|jobs'
                              ur'|m'
                              ur'|mlqt\.tesla\.usability'
                              ur'|mobile\.tesla\.usability'
                              ur'|nagios'
                              ur'|noboard\.chapters'
                              ur'|noc'
                              ur'|observium'
                              ur'|oldusability'
                              ur'|project2'
                              ur'|prototype'
                              ur'|results\.labs'
                              ur'|search'
                              ur'|sitemap'
                              ur'|snapshot3'
                              ur'|stafford'
                              ur'|stats'
                              ur'|status'
                              ur'|svn'
                              ur'|test\.prototype'
                              ur'|torrus'
                              ur'|ubuntu'
                              ur'|wiki-mail'
                              ur'|yongle)\.wikimedia\.org'),
            (ur'\[http://(www\.)?(arbcom\.[a-z]+'
                              ur'|download'
                              ur'|m'
                              ur'|static'
                              ur'|wg\.[a-z]+)\.wikipedia\.org'),
            (ur'\[http://(www\.)?[^@:/]+\.m\.wikipedia\.org'),
            # Preventing test.wikipedia → [[w:test:]]
            (ur'\[//(www\.)?(ten|test|test2)\.wikipedia\.org'),
        ],
        'inside-tags': [
            #
            #  You can occasionally comment some of these exception tags 
            #  under your own risk.
            #
            'blockquote',
            'categorytree',
            'charinsert',
            'comment',
            'dynamicpagelist',
            'gallery',
            'hiero',
            'hyperlink',
            'imagemap',
            'indicator',
            'inputbox',
            'invoke',
            'math',
            'nowiki',
            'pagelist',
            'pagequality',
            'pages',
            'poem',
            'pre',
            'property',
            'score',
            'section',
            'source',
            'syntaxhighlight',
            'templatedata',
            'timeline',
        ]
    }
}
# </nowiki>
# ============================================================================ #



# ============================================================================ #
#
#   +-------------------------+  https://es.wikipedia.org/wiki/User:Invadibot
#   |  Invadibot,  eswiki-08  |  https://meta.wikimedia.org/wiki/User:Invadibot
#   +-------------------------+  http://davidabian.com/invadibot/
#
#   [es] Expresiones regulares para múltiples estandarizaciones en artículos,
#        traducciones y arreglos de formato seguros en Wikipedia en español.
#
# <nowiki>

# NC (nocase) requiere (?i)

P_INICIO         = (ur"{{[\s_]*(?:[Pp]lantilla[\s_]*:"
                              ur"|[Tt]emplate[\s_]*:"
                    ur")?[\s_]*")
P_INICIO_NC      = (ur"{{[\s_]*(?:plantilla[\s_]*:"
                              ur"|template[\s_]*:"
                    ur")?[\s_]*")
P_CITA_INICIO    = (ur"%s[Cc]ita[ _](?:libro"
                                   ur"|noticia"
                                   ur"|publicación"
                                   ur"|web"
                    ur")[^}]*?\|\s*") % P_INICIO
P_CITA_INICIO_NC = (ur"%scita[ _](?:libro"
                                ur"|noticia"
                                ur"|publicación"
                                ur"|web"
                    ur")[^}]*?\|\s*") % P_INICIO_NC

fixes['inva-wp-es'] = {
    'nocase': False,
    'recursive': True,
    'regex': True,
    'msg': {
        '_default': u'Bot: Estandarizaciones y otras mejoras automatizadas',
        'es': u'Bot: [[m:User:Invadibot/scope#eswiki|8]]'
              u' - Estandarizaciones y otras mejoras automatizadas',
    },
    'replacements': [
        
        # Retirada de la plantilla de solicitud de intervención con Invadibot
        (ur'(?i)%sinvadibot[^}]*?}}\s*(.)' % P_INICIO_NC, ur'\1'),

        # Pasar a {{cita libro}}
        (ur'%s[Cc]it[ae][ _]*book([\s_]*[}\|])' % P_INICIO, ur'{{cita libro\1'),
        # Pasar a {{cita noticia}}
        (ur'%s[Cc]it[ae][\s_]*[Nn]ews([\s_]*[}\|])' % P_INICIO, ur'{{cita noticia\1'),
        # Pasar a {{cita publicación}}
        ((ur'%s(?:[Cc]it[ae]r?[ _]*journal'
              ur'|[Cc]it(?:ar|e)[ _]*publicaci[óo]n?'
              ur'|[Cc]itar?[ _]*revista'
              ur'|[Rr]ef[- ]publicaci[óo]n?'
              ur')([\s_]*[}\|])') % P_INICIO, ur'{{cita publicación\1'),
        # Pasar a {{cita vídeo}}
        ((ur'%s(?:[Cc]it[ae]r?[ _]*video'
              ur'|[Cc]it(?:ar|e)[ _]*vídeo'
              ur'|[Cc]it[ae]r?[ _]*[Aa][Vv][ _]*[Mm]edia'
              ur')([\s_]*[}\|])') % P_INICIO, ur'{{cita vídeo\1'),
        # Pasar a {{cita web}}
        ((ur'%s(?:[Cc]ite[ _-]?web(?:site)?'
              ur'|[Cc]itar[ _]web'
              ur'|[Ww]eb[ _-]cite'
              ur'|[Ll]ien[ _-]web'
              ur'|[Rr]ef[ _-](?:internet|web)'
              ur')([\s_]*[}\|])') % P_INICIO, ur'{{cita web\1'),
        
        # Traducción y estandarización indiscriminadas de parámetros para citas
        # libro, noticia, publicación y web
        (ur'(%s)[Aa]ccessdate(\s*=.*?})' % P_CITA_INICIO, ur'\1fechaacceso\2'),
        (ur'(%s)[Aa]ccessmonth(\s*=.*?})' % P_CITA_INICIO, ur'\1mesacceso\2'),
        (ur'(%s)[Aa]ccessmonthday(\s*=.*?})' % P_CITA_INICIO, ur'\1mesacceso\2'),
        (ur'(%s)[Aa]cces+o(\s*=.*?})' % P_CITA_INICIO, ur'\1fechaacceso\2'),
        (ur'(%s)[Aa]ccessyear(\s*=.*?})' % P_CITA_INICIO, ur'\1añoacceso\2'),
        (ur'(%s)[Aa]ny(\s*=.*?})' % P_CITA_INICIO, ur'\1año\2'), #ca
        (ur'(%s)[Aa]rchivedate(\s*=.*?})' % P_CITA_INICIO, ur'\1fechaarchivo\2'),
        (ur'(%s)[Aa]rchiveurl(\s*=.*?})' % P_CITA_INICIO, ur'\1urlarchivo\2'),
        (ur'(%s)[Aa]rxiudata(\s*=.*?})' % P_CITA_INICIO, ur'\1fechaarchivo\2'), #ca
        (ur'(%s)[Aa]rxiuurl(\s*=.*?})' % P_CITA_INICIO, ur'\1urlarchivo\2'), #ca
        (ur'(%s)[Aa]uthor(\d{0,2}\s*=.*?})' % P_CITA_INICIO, ur'\1autor\2'),
        (ur'(%s)[Aa]uthorlink(\d{0,2}\s*=.*?})' % P_CITA_INICIO, ur'\1enlaceautor\2'),
        (ur'(%s)[Aa]utorenllaç(\d{0,2}\s*=.*?})' % P_CITA_INICIO, ur'\1enlaceautor\2'), #ca
        (ur'(%s)[Cc]apítol(\s*=.*?})' % P_CITA_INICIO, ur'\1capítulo\2'), #ca
        (ur'(%s)[Cc]hapter(\s*=.*?})' % P_CITA_INICIO, ur'\1capítulo\2'),
        (ur'(%s)[Cc]hapterurl(\s*=.*?})' % P_CITA_INICIO, ur'\1urlcapítulo\2'),
        (ur'(%s)[Cc]itació(\s*=.*?})' % P_CITA_INICIO, ur'\1cita\2'), #ca
        (ur'(%s)[Cc]ittà(\s*=.*?})' % P_CITA_INICIO, ur'\1ubicación\2'),
        (ur'(%s)[Cc]oauthors(\s*=.*?})' % P_CITA_INICIO, ur'\1coautores\2'),
        (ur'(%s)[Cc]oautors(\s*=.*?})' % P_CITA_INICIO, ur'\1coautores\2'), #ca
        (ur'(%s)[Cc]ol·lecció(\s*=.*?})' % P_CITA_INICIO, ur'\1obra\2'), #ca
        (ur'(%s)[Cc]ognom(\d{0,2}\s*=.*?})' % P_CITA_INICIO, ur'\1apellido\2'), #ca
        (ur'(%s)[Cc]onsulta(\s*=.*?})' % P_CITA_INICIO, ur'\1fechaacceso\2'), #ca
        (ur'(%s)[Dd]ate(\s*=.*?})' % P_CITA_INICIO, ur'\1fecha\2'),
        (ur'(%s)[Ee]dici[óo](\s*=.*?})' % P_CITA_INICIO, ur'\1edición\2'), #ca
        (ur'(%s)[Ee]dition(\s*=.*?})' % P_CITA_INICIO, ur'\1edición\2'),
        (ur'(%s)[Ee]nllaçautor(\d{0,2}\s*=.*?})' % P_CITA_INICIO, ur'\1enlaceautor\2'), #ca
        (ur'(%s)[Ff]echa[ _]de[ _]acceso(\s*=.*?})' % P_CITA_INICIO, ur'\1fechaacceso\2'),
        (ur'(%s)[Ff]echaaacceso(\s*=.*?})' % P_CITA_INICIO, ur'\1fechaacceso\2'),
        (ur'(%s)[Ff]irst(\s*=.*?})' % P_CITA_INICIO, ur'\1nombre\2'),
        (ur'(%s)[Ff]ormat(\s*=.*?})' % P_CITA_INICIO, ur'\1formato\2'),
        (ur'(%s)[Ii][Dd](\s*=.*?})' % P_CITA_INICIO, ur'\1id\2'),
        (ur'(%s)[Ii][Ss][Bb][Nn](\s*=.*?})' % P_CITA_INICIO, ur'\1isbn\2'),
        (ur'(%s)[Ii]ssue(\s*=.*?})' % P_CITA_INICIO, ur'\1número\2'),
        (ur'(%s)[Jj]ournal(\s*=.*?})' % P_CITA_INICIO, ur'\1publicación\2'),
        (ur'(%s)[Ll]anguage(\s*=.*?})' % P_CITA_INICIO, ur'\1idioma\2'),
        (ur'(%s)[Ll]ast(\s*=.*?})' % P_CITA_INICIO, ur'\1apellido\2'),
        (ur'(%s)[Ll]aydate(\s*=.*?})' % P_CITA_INICIO, ur'\1fechaprofano\2'),
        (ur'(%s)[Ll]aysource(\s*=.*?})' % P_CITA_INICIO, ur'\1fuenteprofano\2'),
        (ur'(%s)[Ll]aysummary(\s*=.*?})' % P_CITA_INICIO, ur'\1resumenprofano\2'),
        (ur'(%s)[Ll]lengua(\s*=.*?})' % P_CITA_INICIO, ur'\1idioma\2'), #ca
        (ur'(%s)[Ll]loc(\s*=.*?})' % P_CITA_INICIO, ur'\1ubicación\2'), #ca
        (ur'(%s)[Ll]ocation(\s*=.*?})' % P_CITA_INICIO, ur'\1ubicación\2'),
        (ur'(%s)[Ll]ugar(\s*=.*?})' % P_CITA_INICIO, ur'\1ubicación\2'),
        (ur'(%s)[Mm]onth(\s*=.*?})' % P_CITA_INICIO, ur'\1mes\2'),
        (ur'(%s)[Nn]om(\d{0,2}\s*=.*?})' % P_CITA_INICIO, ur'\1nombre\2'), #ca
        (ur'(%s)[Oo]thers(\s*=.*?})' % P_CITA_INICIO, ur'\1otros\2'),
        (ur'(%s)[Pp]age(\s*=.*?})' % P_CITA_INICIO, ur'\1página\2'),
        (ur'(%s)[Pp]ages(\s*=.*?})' % P_CITA_INICIO, ur'\1páginas\2'),
        (ur'(%s)[Pp]àgina(\s*=.*?})' % P_CITA_INICIO, ur'\1página\2'), #ca
        (ur'(%s)[Pp][aà]gines(\s*=.*?})' % P_CITA_INICIO, ur'\1páginas\2'), #ca
        (ur'(%s)[Pp]ublicaci[óo](\s*=.*?})' % P_CITA_INICIO, ur'\1publicación\2'), #ca
        (ur'(%s)[Pp]ublisher(\s*=.*?})' % P_CITA_INICIO, ur'\1editorial\2'),
        (ur'(%s)[Qq]uote(\s*=.*?})' % P_CITA_INICIO, ur'\1cita\2'),
        (ur'(%s)[Tt]itle(\s*=.*?})' % P_CITA_INICIO, ur'\1título\2'),
        (ur'(%s)[Tt][íi]tol(\s*=.*?})' % P_CITA_INICIO, ur'\1título\2'), #ca
        (ur'(%s)[Uu]bicacion(\s*=.*?})' % P_CITA_INICIO, ur'\1ubicación\2'),
        (ur'(%s)[Uu]rlcapítol(\s*=.*?})' % P_CITA_INICIO, ur'\1urlcapítulo\2'), #ca
        (ur'(%s)[Vv][ií]ncu?lo[ _]autora?(\s*=.*?})' % P_CITA_INICIO, ur'\1enlaceautor\2'),
        (ur'(%s)[Vv]olum(\s*=.*?})' % P_CITA_INICIO, ur'\1volumen\2'), #ca
        (ur'(%s)[Vv]olume(\s*=.*?})' % P_CITA_INICIO, ur'\1volumen\2'),
        (ur'(%s)[Vv]olúmen(\s*=.*?})' % P_CITA_INICIO, ur'\1volumen\2'),
        (ur'(%s)[Vv]olumem(\s*=.*?})' % P_CITA_INICIO, ur'\1volumen\2'),
        (ur'(%s)[Ww]ork(\s*=.*?})' % P_CITA_INICIO, ur'\1obra\2'),
        (ur'(%s)[Yy]ear(\s*=.*?})' % P_CITA_INICIO, ur'\1año\2'),
        (ur'(%s)U(?:RL|rl)(\s*=.*?})' % P_CITA_INICIO, ur'\1url\2'),

        # Traducir ubicaciones (en orden alfabético en español)
        (ur'(?i)(%subicación\s*=\s*)(?:bagh?dad)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1Bagdad\2'),
        (ur'(?i)(%subicación\s*=\s*)(?:[ei]sta[mn]bul)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1Estambul\2'),
        (ur'(?i)(%subicación\s*=\s*)(?:londres|london)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1Londres\2'),
        (ur'(?i)(%subicación\s*=\s*)(?:m[éeè][jx]ico,? ?d\.? ?f\.?|mexico city)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1México,&nbsp;D.&nbsp;F.\2'),
        (ur'(?i)(%subicación\s*=\s*)(?:mosc[úuù]|moscow|moskva)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1Moscú\2'),
        (ur'(?i)(%subicación\s*=\s*)(?:nanjing|nank[íiì]ng?)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1Nankín\2'),
        (ur'(?i)(%subicación\s*=\s*)(?:nueva delh?i|new delhi)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1Nueva&nbsp;Delhi\2'),
        (ur'(?i)(%subicación\s*=\s*)(?:nue[bv]a york?|new york(?: city)?)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1Nueva&nbsp;York\2'),
        (ur'(?i)(%subicación\s*=\s*)(?:beijing|pek[íiì]ng?)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1Pekín\2'),
        (ur'(?i)(%subicación\s*=\s*)(?:seo?[úuù]l)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1Seúl\2'),
        (ur'(?i)(%subicación\s*=\s*)(?:sevill[ae])(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1Sevilla\2'),
        (ur'(?i)(%subicación\s*=\s*)(?:sh?angh?[áaà]i)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1Shanghái\2'),
        (ur'(?i)(%subicación\s*=\s*)(?:tehe?r[áaà]n)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1Teherán\2'),
        (ur'(?i)(%subicación\s*=\s*)(?:tok[iy]o)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1Tokio\2'),

        # Traducir idiomas (en orden alfabético en español)
            # Traducciones de "alemán" al español
            (ur'(?i)(%sidioma\s*=\s*)german(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1alemán\2'),
            (ur'(?i)(%sidioma\s*=\s*)alem[ãa]o(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1alemán\2'),
            (ur'(?i)(%sidioma\s*=\s*)all?emande?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1alemán\2'),
            (ur'(?i)(%sidioma\s*=\s*)all?em[áa]ny?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1alemán\2'),
            (ur'(?i)(%sidioma\s*=\s*)de[iu]tsche?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1alemán\2'),
            (ur'(?i)(%sidioma\s*=\s*)duits(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1alemán\2'),
            (ur'(?i)(%sidioma\s*=\s*)gearm[áa]inis(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1alemán\2'),
            (ur'(?i)(%sidioma\s*=\s*)germanaj(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1alemán\2'),
            (ur'(?i)(%sidioma\s*=\s*)tedesco(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1alemán\2'),
                # En inglés con enlace
                (ur'(?i)(%sidioma\s*=\s*)\[\[\s*german[ _]language\s*\|\s*german\s*\]\](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1[[Idioma alemán|alemán]]\2'),

            # Traducciones de "catalán" al español
            (ur'(?i)(%sidioma\s*=\s*)catal[ãáaà]o?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1catalán\2'),
            (ur'(?i)(%sidioma\s*=\s*)catal[áaà]n[aeio]?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1catalán\2'),
            (ur'(?i)(%sidioma\s*=\s*)catal[óo]inis(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1catalán\2'),
            (ur'(?i)(%sidioma\s*=\s*)catalaanse?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1catalán\2'),
            (ur'(?i)(%sidioma\s*=\s*)katalana?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1catalán\2'),
            (ur'(?i)(%sidioma\s*=\s*)katalanaren(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1catalán\2'),
            (ur'(?i)(%sidioma\s*=\s*)katalanische?n?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1catalán\2'),
            (ur'(?i)(%sidioma\s*=\s*)katalanska(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1catalán\2'),
            (ur'(?i)(%sidioma\s*=\s*)katalunaj?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1catalán\2'),
                # En inglés con enlace
                (ur'(?i)(%sidioma\s*=\s*)\[\[\s*catalan[ _]language\s*\|\s*catalan\s*\]\](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1[[Idioma catalán|catalán]]\2'),

            # Traducciones de "español" al español
            (ur'(?i)(%sidioma\s*=\s*)castell[àa](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1español\2'),
            (ur'(?i)(%sidioma\s*=\s*)espagnole?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1español\2'),
            (ur'(?i)(%sidioma\s*=\s*)espainiako(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1español\2'),
            (ur'(?i)(%sidioma\s*=\s*)espan[hiy]?ol(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1español\2'),
            (ur'(?i)(%sidioma\s*=\s*)españ[óo]l(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1español\2'),
            (ur'(?i)(%sidioma\s*=\s*)hispan[ao](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1español\2'),
            (ur'(?i)(%sidioma\s*=\s*)sp[áaà]innis(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1español\2'),
            (ur'(?i)(%sidioma\s*=\s*)spaans(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1español\2'),
            (ur'(?i)(%sidioma\s*=\s*)spagnolo(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1español\2'),
            (ur'(?i)(%sidioma\s*=\s*)spanische?n?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1español\2'),
            (ur'(?i)(%sidioma\s*=\s*)spanish(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1español\2'),
                # En inglés con enlace
                (ur'(?i)(%sidioma\s*=\s*)\[\[\s*spanish[ _]language\s*\|\s*spanish\s*\]\](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1[[Idioma español|español]]\2'),

            # Traducciones de "francés" al español
            (ur'(?i)(%sidioma\s*=\s*)french(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1francés\2'),
            (ur'(?i)(%sidioma\s*=\s*)ffrangeg(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1francés\2'),
            (ur'(?i)(%sidioma\s*=\s*)fraincis(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1francés\2'),
            (ur'(?i)(%sidioma\s*=\s*)fran[çc]aise?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1francés\2'),
            (ur'(?i)(%sidioma\s*=\s*)franc[éêèe]se?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1francés\2'),
            (ur'(?i)(%sidioma\s*=\s*)francaj(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1francés\2'),
            (ur'(?i)(%sidioma\s*=\s*)frans(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1francés\2'),
            (ur'(?i)(%sidioma\s*=\s*)franska(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1francés\2'),
            (ur'(?i)(%sidioma\s*=\s*)frantsesa?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1francés\2'),
            (ur'(?i)(%sidioma\s*=\s*)franz[öo]sische?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1francés\2'),
                # En inglés con enlace
                (ur'(?i)(%sidioma\s*=\s*)\[\[\s*french[ _]language\s*\|\s*french\s*\]\](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1[[Idioma francés|francés]]\2'),
            
            # Traducciones de "inglés" al español
            (ur'(?i)(%sidioma\s*=\s*)angl[éèe]s(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1inglés\2'),
            (ur'(?i)(%sidioma\s*=\s*)anglais(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1inglés\2'),
            (ur'(?i)(%sidioma\s*=\s*)anglaj(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1inglés\2'),
            (ur'(?i)(%sidioma\s*=\s*)anglicus(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1inglés\2'),
            (ur'(?i)(%sidioma\s*=\s*)b[ée]arla(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1inglés\2'),
            (ur'(?i)(%sidioma\s*=\s*)engels(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1inglés\2'),
            (ur'(?i)(%sidioma\s*=\s*)engelska(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1inglés\2'),
            (ur'(?i)(%sidioma\s*=\s*)englez(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1inglés\2'),
            (ur'(?i)(%sidioma\s*=\s*)englische?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1inglés\2'),
            (ur'(?i)(%sidioma\s*=\s*)english(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1inglés\2'),
            (ur'(?i)(%sidioma\s*=\s*)ingl[éêèe]se?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1inglés\2'),
            (ur'(?i)(%sidioma\s*=\s*)saesneg(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1inglés\2'),
                # En inglés con enlace
                (ur'(?i)(%sidioma\s*=\s*)\[\[\s*english[ _]language\s*\|\s*english\s*\]\](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1[[Idioma inglés|inglés]]\2'),
            
            # Traducciones de "italiano" al español
            (ur'(?i)(%sidioma\s*=\s*)iodáilis(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1italiano\2'),
            (ur'(?i)(%sidioma\s*=\s*)ital[ao]j(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1italiano\2'),
            (ur'(?i)(%sidioma\s*=\s*)itali[áaà](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1italiano\2'),
            (ur'(?i)(%sidioma\s*=\s*)itali[ae]no?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1italiano\2'),
            (ur'(?i)(%sidioma\s*=\s*)italiaa?ns(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1italiano\2'),
            (ur'(?i)(%sidioma\s*=\s*)italienische?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1italiano\2'),
            (ur'(?i)(%sidioma\s*=\s*)italiensk(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1italiano\2'),
            (ur'(?i)(%sidioma\s*=\s*)taljan(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1italiano\2'),
                # En inglés con enlace
                (ur'(?i)(%sidioma\s*=\s*)\[\[\s*italian[ _]language\s*\|\s*italian\s*\]\](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1[[Idioma italiano|italiano]]\2'),
            
            # Traducciones de "neerlandés" al español
            (ur'(?i)(%sidioma\s*=\s*)dutch(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1neerlandés\2'),
            (ur'(?i)(%sidioma\s*=\s*)nederlaa?nds?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1neerlandés\2'),
            (ur'(?i)(%sidioma\s*=\s*)niederl[aä]ndische?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1neerlandés\2'),
            (ur'(?i)(%sidioma\s*=\s*)niderlandzki(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1neerlandés\2'),
            (ur'(?i)(%sidioma\s*=\s*)n[éeè][éeè]?rland[aéeè]i?[sz][aăe]?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1neerlandés\2'),
            (ur'(?i)(%sidioma\s*=\s*)olandese?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1neerlandés\2'),
                # En inglés con enlace
                (ur'(?i)(%sidioma\s*=\s*)\[\[\s*dutch[ _]language\s*\|\s*dutch\s*\]\](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1[[Idioma neerlandés|neerlandés]]\2'),

            # Traducciones de "portugués" al español
            (ur'(?i)(%sidioma\s*=\s*)portugu?[éêèe]e?s[ae]?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1portugués\2'),
            (ur'(?i)(%sidioma\s*=\s*)portaing[ée]ilis(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1portugués\2'),
            (ur'(?i)(%sidioma\s*=\s*)portogh[êéèe]se?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1portugués\2'),
            (ur'(?i)(%sidioma\s*=\s*)portugaise?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1portugués\2'),
            (ur'(?i)(%sidioma\s*=\s*)portugala(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1portugués\2'),
            (ur'(?i)(%sidioma\s*=\s*)portugiesische?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1portugués\2'),
                # En inglés con enlace
                (ur'(?i)(%sidioma\s*=\s*)\[\[\s*portuguese[ _]language\s*\|\s*portuguese\s*\]\](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1[[Idioma portugués|portugués]]\2'),

            # Traducciones de "ruso" al español
            (ur'(?i)(%sidioma\s*=\s*)rusa?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1ruso\2'),
            (ur'(?i)(%sidioma\s*=\s*)errusiera(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1ruso\2'),
            (ur'(?i)(%sidioma\s*=\s*)rúisis(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1ruso\2'),
            (ur'(?i)(%sidioma\s*=\s*)russ[eo](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1ruso\2'),
            (ur'(?i)(%sidioma\s*=\s*)russiann?e?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1ruso\2'),
            (ur'(?i)(%sidioma\s*=\s*)russische?n?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1ruso\2'),
            (ur'(?i)(%sidioma\s*=\s*)russkaya(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1ruso\2'),
            (ur'(?i)(%sidioma\s*=\s*)russkiy(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1ruso\2'),
            (ur'(?i)(%sidioma\s*=\s*)rwsia(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1ruso\2'),
            (ur'(?i)(%sidioma\s*=\s*)ryska(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1ruso\2'),
            (ur'(?i)(%sidioma\s*=\s*)русская(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1ruso\2'),
            (ur'(?i)(%sidioma\s*=\s*)русский(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1ruso\2'),
                # En inglés con enlace
                (ur'(?i)(%sidioma\s*=\s*)\[\[\s*russian[ _]language\s*\|\s*russian\s*\]\](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1[[Idioma ruso|ruso]]\2'),

            # Traducciones de "sueco" al español
            (ur'(?i)(%sidioma\s*=\s*)schwedische?n?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1sueco\2'),
            (ur'(?i)(%sidioma\s*=\s*)su[ée]co?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1sueco\2'),
            (ur'(?i)(%sidioma\s*=\s*)su[éeè]doise?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1sueco\2'),
            (ur'(?i)(%sidioma\s*=\s*)sualainnis(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1sueco\2'),
            (ur'(?i)(%sidioma\s*=\s*)suediako(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1sueco\2'),
            (ur'(?i)(%sidioma\s*=\s*)suediarrak?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1sueco\2'),
            (ur'(?i)(%sidioma\s*=\s*)sved[ao]j?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1sueco\2'),
            (ur'(?i)(%sidioma\s*=\s*)svedese(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1sueco\2'),
            (ur'(?i)(%sidioma\s*=\s*)svensk[ae]?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1sueco\2'),
            (ur'(?i)(%sidioma\s*=\s*)swed[ei]g(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1sueco\2'),
            (ur'(?i)(%sidioma\s*=\s*)swedish(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1sueco\2'),
            (ur'(?i)(%sidioma\s*=\s*)swedish(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1sueco\2'),
                # En inglés con enlace
                (ur'(?i)(%sidioma\s*=\s*)\[\[\s*swedish[ _]language\s*\|\s*swedish\s*\]\](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1[[Idioma sueco|sueco]]\2'),

            # Más traducciones, solo del inglés al español, y estandarización
            (ur'(?i)(%sidioma\s*=\s*)bengal[íi](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1bengalí\2'),
            (ur'(?i)(%sidioma\s*=\s*)chin(?:ese|o)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1chino\2'),
            (ur'(?i)(%sidioma\s*=\s*)[ck]ore[áa]no?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1coreano\2'),
            (ur'(?i)(%sidioma\s*=\s*)jap(?:anese|on[éeè]s)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1japonés\2'),
            (ur'(?i)(%sidioma\s*=\s*)javan[éeè]se?(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1javanés\2'),
            (ur'(?i)(%sidioma\s*=\s*)mandar[íiì]n(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1mandarín\2'),
            (ur'(?i)(%sidioma\s*=\s*)marath?[íiì](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1maratí\2'),
            (ur'(?i)(%sidioma\s*=\s*)telug[úuù](\s*[}\|])' % P_CITA_INICIO_NC, ur'\1telugú\2'),

        # Estandarizar y traducir fechas al español
            # En plantillas de citas
                # AAAA[-/\\\.]MM[-/\\\.]DD → DD-MM-AAAA
                (ur'({{[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)([12]\d\d\d)[-/\\\.](\d\d?)[-/\\\.](\d\d?)(\s*[}\|])', ur'\1\4-\3-\2\5'),

                # Estandarizar y traducir meses aislados
                #  Ejemplo: {{cita web|mes=January}} → {{cita web|mes=enero}}
                #  Idiomas garantizados: es, en, fr, sv
                (ur'(?i)(%s\bmes\s*=\s*)(?:en[éeè]ro|januar[iy]|janvier)' % P_CITA_INICIO_NC, ur'\1enero'),
                (ur'(?i)(%s\bmes\s*=\s*)(?:febr[éeè]ro|februar[iy]|f[éeè]vrier)' % P_CITA_INICIO_NC, ur'\1febrero'),
                (ur'(?i)(%s\bmes\s*=\s*)(?:m[áaà]rzo|march|mars)' % P_CITA_INICIO_NC, ur'\1marzo'),
                (ur'(?i)(%s\bmes\s*=\s*)(?:abr[íiì]l|april|avril)' % P_CITA_INICIO_NC, ur'\1abril'),
                (ur'(?i)(%s\bmes\s*=\s*)(?:m[áaà]yo|ma[ijy])' % P_CITA_INICIO_NC, ur'\1mayo'),
                (ur'(?i)(%s\bmes\s*=\s*)(?:j[úuù]nio|jun[ei]|juin)' % P_CITA_INICIO_NC, ur'\1junio'),
                (ur'(?i)(%s\bmes\s*=\s*)(?:j[úuù]lio|jul[iy]|juillet)' % P_CITA_INICIO_NC, ur'\1julio'),
                (ur'(?i)(%s\bmes\s*=\s*)(?:ag[óoò]sto|augusti?|ao[ûu]t)' % P_CITA_INICIO_NC, ur'\1agosto'),
                (ur'(?i)(%s\bmes\s*=\s*)(?:septi[éeè]mbre|september|septembre)' % P_CITA_INICIO_NC, ur'\1septiembre'),
                (ur'(?i)(%s\bmes\s*=\s*)(?:oct[úuù]bre|o[ck]tober|octobre)' % P_CITA_INICIO_NC, ur'\1octubre'),
                (ur'(?i)(%s\bmes\s*=\s*)(?:novi[éeè]mbre|november|novembre)' % P_CITA_INICIO_NC, ur'\1noviembre'),
                (ur'(?i)(%s\bmes\s*=\s*)(?:dici[éeè]mbre|december|d[éeè]cembre)' % P_CITA_INICIO_NC, ur'\1diciembre'),

                # Estandarizar y traducir fechas con palabras
                #  Idiomas garantizados: es, en, fr, sv
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:en[éeè]ro|januar[iy]|janvier)\b' % P_CITA_INICIO_NC, ur'\1 de enero'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:febr[éeè]ro|februar[iy]|f[éeè]vrier)\b' % P_CITA_INICIO_NC, ur'\1 de febrero'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:m[áaà]rzo|march|mars)\b' % P_CITA_INICIO_NC, ur'\1 de marzo'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:abr[íiì]l|april|avril)\b' % P_CITA_INICIO_NC, ur'\1 de abril'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:m[áaà]yo|ma[ijy])\b' % P_CITA_INICIO_NC, ur'\1 de mayo'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:j[úuù]nio|jun[ei]|juin)\b' % P_CITA_INICIO_NC, ur'\1 de junio'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:j[úuù]lio|jul[iy]|juillet)\b' % P_CITA_INICIO_NC, ur'\1 de julio'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:ag[óoò]sto|augusti?|ao[ûu]t)\b' % P_CITA_INICIO_NC, ur'\1 de agosto'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:septi[éeè]mbre|september|septembre)\b' % P_CITA_INICIO_NC, ur'\1 de septiembre'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:oct[úuù]bre|o[ck]tober|octobre)\b' % P_CITA_INICIO_NC, ur'\1 de octubre'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:novi[éeè]mbre|november|novembre)\b' % P_CITA_INICIO_NC, ur'\1 de noviembre'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:dici[éeè]mbre|december|d[éeè]cembre)\b' % P_CITA_INICIO_NC, ur'\1 de diciembre'),

                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:en[éeè](?:ro)?|jan(?:uar[iy])?|janvier)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1 de enero de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:feb(?:r[éeè]ro)?|februar[iy]|f[éeè]v(?:rier)?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1 de febrero de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:m[áaà]r(?:zo)?|march|mars)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1 de marzo de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:abr(?:[íiì]l)?|apr(?:il)?|avr(?:il)?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1 de abril de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:m[áaà]yo?|ma[ijy])[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1 de mayo de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:j[úuù]n(?:io)?|jun[ei]|juin)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1 de junio de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:j[úuù]l(?:io)?|jul[iy]|juil(?:let)?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1 de julio de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:ag[óoò](?:sto)?|aug(?:usti?)?|ao[ûu]t)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1 de agosto de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:sept?(?:i[éeè]mbre)?|september|septembre)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1 de septiembre de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:oct[úuù]bre|o[ck]t(?:ober)?|octobre)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1 de octubre de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:nov(?:i[éeè]mbre)?|november|novembre)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1 de noviembre de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:dic(?:i[éeè]mbre)?|december|d[éeè]c(?:embre)?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1 de diciembre de \2\3'),

                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:en[éeè]ro|januar[iy]|janvier)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1enero de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:febr[éeè]ro|februar[iy]|f[éeè]vrier)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1febrero de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:m[áaà]rzo|march|mars)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1marzo de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:abr[íiì]l|april|avril)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1abril de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:m[áaà]yo|ma[ijy])[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1mayo de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:j[úuù]nio|jun[ei]|juin)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1junio de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:j[úuù]lio|jul[iy]|juillet)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1julio de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:ag[óoò]sto|augusti?|ao[ûu]t)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1agosto de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:septi[éeè]mbre|september|septembre)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1septiembre de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:oct[úuù]bre|o[ck]tober|octobre)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1octubre de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:novi[éeè]mbre|november|novembre)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1noviembre de \2\3'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:dici[éeè]mbre|december|d[éeè]cembre)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1diciembre de \2\3'),

                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:en[éeè]ro|januar[iy]|janvier)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1\2 de enero de \3\4'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:febr[éeè]ro|februar[iy]|f[éeè]vrier)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1\2 de febrero de \3\4'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:m[áaà]rzo|march|mars)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1\2 de marzo de \3\4'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:abr[íiì]l|april|avril)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1\2 de abril de \3\4'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:m[áaà]yo|ma[ijy])[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1\2 de mayo de \3\4'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:j[úuù]nio|jun[ei]|juin)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1\2 de junio de \3\4'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:j[úuù]lio|jul[iy]|juillet)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1\2 de julio de \3\4'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:ag[óoò]sto|augusti?|ao[ûu]t)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1\2 de agosto de \3\4'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:septi[éeè]mbre|september|septembre)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1\2 de septiembre de \3\4'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:oct[úuù]bre|o[ck]tober|octobre)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1\2 de octubre de \3\4'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:novi[éeè]mbre|november|novembre)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1\2 de noviembre de \3\4'),
                (ur'(?i)(%s(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:dici[éeè]mbre|december|d[éeè]cembre)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])' % P_CITA_INICIO_NC, ur'\1\2 de diciembre de \3\4'),

            # En cualquier ámbito
                # Aplicar minúscula inicial al mes, retirar artículo al año y
                # suprimir posible sustantivo "día" en años posteriores al 99
                #  Ejemplo: día 12 de Marzo del 1456 → 12 de marzo de 1456
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Ee]nero\s+del?\s+(\[\[)?\s?(\d{4}[^\d])', ur'\2enero de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Ff]ebrero\s+del?\s+(\[\[)?\s?(\d{4}[^\d])', ur'\2febrero de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Mm]arzo\s+del?\s+(\[\[)?\s?(\d{4}[^\d])', ur'\2marzo de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Aa]bril\s+del?\s+(\[\[)?\s?(\d{4}[^\d])', ur'\2abril de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Mm]ayo\s+del?\s+(\[\[)?\s?(\d{4}[^\d])', ur'\2mayo de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Jj]unio\s+del?\s+(\[\[)?\s?(\d{4}[^\d])', ur'\2junio de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Jj]ulio\s+del?\s+(\[\[)?\s?(\d{4}[^\d])', ur'\2julio de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Aa]gosto\s+del?\s+(\[\[)?\s?(\d{4}[^\d])', ur'\2agosto de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Ss]eptiembre\s+del?\s+(\[\[)?\s?(\d{4}[^\d])', ur'\2septiembre de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Ss]etiembre\s+del?\s+(\[\[)?\s?(\d{4}[^\d])', ur'\2setiembre de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Oo]ctubre\s+del?\s+(\[\[)?\s?(\d{4}[^\d])', ur'\2octubre de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Nn]oviembre\s+del?\s+(\[\[)?\s?(\d{4}[^\d])', ur'\2noviembre de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Dd]iciembre\s+del?\s+(\[\[)?\s?(\d{4}[^\d])', ur'\2diciembre de \3\4'),

                # Suprimir término "año" en años posteriores al 999
                #  Ejemplo: 12 de marzo del año 1456 → 12 de marzo de 1456
                (ur'(\d\d?\sde\s)\s*enero\s+del\s+año\s+(\[\[)?\s?([12]\d\d\d)', ur'\1enero de \2\3'),
                (ur'(\d\d?\sde\s)\s*febrero\s+del\s+año\s+(\[\[)?\s?([12]\d\d\d)', ur'\1febrero de \2\3'),
                (ur'(\d\d?\sde\s)\s*marzo\s+del\s+año\s+(\[\[)?\s?([12]\d\d\d)', ur'\1marzo de \2\3'),
                (ur'(\d\d?\sde\s)\s*abril\s+del\s+año\s+(\[\[)?\s?([12]\d\d\d)', ur'\1abril de \2\3'),
                (ur'(\d\d?\sde\s)\s*mayo\s+del\s+año\s+(\[\[)?\s?([12]\d\d\d)', ur'\1mayo de \2\3'),
                (ur'(\d\d?\sde\s)\s*junio\s+del\s+año\s+(\[\[)?\s?([12]\d\d\d)', ur'\1junio de \2\3'),
                (ur'(\d\d?\sde\s)\s*julio\s+del\s+año\s+(\[\[)?\s?([12]\d\d\d)', ur'\1julio de \2\3'),
                (ur'(\d\d?\sde\s)\s*agosto\s+del\s+año\s+(\[\[)?\s?([12]\d\d\d)', ur'\1agosto de \2\3'),
                (ur'(\d\d?\sde\s)\s*septiembre\s+del\s+año\s+(\[\[)?\s?([12]\d\d\d)', ur'\1septiembre de \2\3'),
                (ur'(\d\d?\sde\s)\s*setiembre\s+del\s+año\s+(\[\[)?\s?([12]\d\d\d)', ur'\1setiembre de \2\3'),
                (ur'(\d\d?\sde\s)\s*octubre\s+del\s+año\s+(\[\[)?\s?([12]\d\d\d)', ur'\1octubre de \2\3'),
                (ur'(\d\d?\sde\s)\s*noviembre\s+del\s+año\s+(\[\[)?\s?([12]\d\d\d)', ur'\1noviembre de \2\3'),
                (ur'(\d\d?\sde\s)\s*diciembre\s+del\s+año\s+(\[\[)?\s?([12]\d\d\d)', ur'\1diciembre de \2\3'),

                # Suprimir cero a la izquierda en fechas con palabras
                #  Ejemplo: 01 de febrero de 1996 → 1 de febrero de 1996
                (ur'([^\d])0(\d\s+de\s+)enero\s+de\s+(\[\[)?\s?(\d{4}[^\d])', ur'\1\2enero de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)febrero\s+de\s+(\[\[)?\s?(\d{4}[^\d])', ur'\1\2febrero de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)marzo\s+de\s+(\[\[)?\s?(\d{4}[^\d])', ur'\1\2marzo de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)abril\s+de\s+(\[\[)?\s?(\d{4}[^\d])', ur'\1\2abril de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)mayo\s+de\s+(\[\[)?\s?(\d{4}[^\d])', ur'\1\2mayo de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)junio\s+de\s+(\[\[)?\s?(\d{4}[^\d])', ur'\1\2junio de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)julio\s+de\s+(\[\[)?\s?(\d{4}[^\d])', ur'\1\2julio de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)agosto\s+de\s+(\[\[)?\s?(\d{4}[^\d])', ur'\1\2agosto de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)septiembre\s+de\s+(\[\[)?\s?(\d{4}[^\d])', ur'\1\2septiembre de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)setiembre\s+de\s+(\[\[)?\s?(\d{4}[^\d])', ur'\1\2setiembre de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)octubre\s+de\s+(\[\[)?\s?(\d{4}[^\d])', ur'\1\2octubre de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)noviembre\s+de\s+(\[\[)?\s?(\d{4}[^\d])', ur'\1\2noviembre de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)diciembre\s+de\s+(\[\[)?\s?(\d{4}[^\d])', ur'\1\2diciembre de \3\4'),

                # Aplicar versalita y espacio indivisible en siglos
                # con especificación de antes o después de Cristo
                ##
                #
                #  POR DESARROLLAR
                #
                ##
                #(ur'([Ss]iglo(?:&nbsp| +)(?:[IVXivx]{0,5}))I((?:[IVXivx]{0,5})(?:&nbsp;| +)?[AaDd]\.?(?:&nbsp;| +)?[Cc]\.?[\)\s—–-])', ur'\1i\2'),
                #(ur'([Ss]iglo(?:&nbsp| +)(?:[IVXivx]{0,5}))V((?:[IVXivx]{0,5})(?:&nbsp;| +)?[AaDd]\.?(?:&nbsp;| +)?[Cc]\.?[\)\s—–-])', ur'\1v\2'),
                #(ur'([Ss]iglo(?:&nbsp| +)(?:[IVXivx]{0,5}))X((?:[IVXivx]{0,5})(?:&nbsp;| +)?[AaDd]\.?(?:&nbsp;| +)?[Cc]\.?[\)\s—–-])', ur'\1x\2'),
                #(ur'([Ss]iglo)(?:&nbsp| +)([ivx]+)(?:&nbsp;| +)?[Aa]\.?(?:&nbsp;| +)?[Cc]\.?([\)\s—–-])', ur'\1&nbsp;{{versalita|\2}}&nbsp;a.&nbsp;C.\3'),
                #(ur'([Ss]iglo)(?:&nbsp| +)([ivx]+)(?:&nbsp;| +)?[Dd]\.?(?:&nbsp;| +)?[Cc]\.?([\)\s—–-])', ur'\1&nbsp;{{versalita|\2}}&nbsp;d.&nbsp;C.\3'),
                #(ur'([Ss]iglos?(?:&nbsp| +)(?:[IVXivx]{0,5}))I((?:[IVXivx]{0,5})-[IVXivx]+(?:&nbsp;| +)?[AaDd]\.?(?:&nbsp;| +)?[Cc]\.?[\)\s—–-])', ur'\1i\2'),
                #(ur'([Ss]iglos?(?:&nbsp| +)(?:[IVXivx]{0,5}))V((?:[IVXivx]{0,5})-[IVXivx]+(?:&nbsp;| +)?[AaDd]\.?(?:&nbsp;| +)?[Cc]\.?[\)\s—–-])', ur'\1v\2'),
                #(ur'([Ss]iglos?(?:&nbsp| +)(?:[IVXivx]{0,5}))X((?:[IVXivx]{0,5})-[IVXivx]+(?:&nbsp;| +)?[AaDd]\.?(?:&nbsp;| +)?[Cc]\.?[\)\s—–-])', ur'\1x\2'),
                #(ur'([Ss]iglos?(?:&nbsp| +)[IVXivx]+-(?:[IVXivx]{0,5}))I((?:[IVXivx]{0,5})(?:&nbsp;| +)?[AaDd]\.?(?:&nbsp;| +)?[Cc]\.?[\)\s—–-])', ur'\1i\2'),
                #(ur'([Ss]iglos?(?:&nbsp| +)[IVXivx]+-(?:[IVXivx]{0,5}))V((?:[IVXivx]{0,5})(?:&nbsp;| +)?[AaDd]\.?(?:&nbsp;| +)?[Cc]\.?[\)\s—–-])', ur'\1v\2'),
                #(ur'([Ss]iglos?(?:&nbsp| +)[IVXivx]+-(?:[IVXivx]{0,5}))X((?:[IVXivx]{0,5})(?:&nbsp;| +)?[AaDd]\.?(?:&nbsp;| +)?[Cc]\.?[\)\s—–-])', ur'\1x\2'),
                #(ur'([Ss]iglo)s?(?:&nbsp| +)([ivx]{1,6})-([ivx]{1,6})(?:&nbsp;| +)?[Aa]\.?(?:&nbsp;| +)?[Cc]\.?([\)\s—–-])', ur'\1s&nbsp;{{versalita|\2}}-{{versalita|\3}}&nbsp;a.&nbsp;C.\4'),
                #(ur'([Ss]iglo)s?(?:&nbsp| +)([ivx]{1,6})-([ivx]{1,6})(?:&nbsp;| +)?[Dd]\.?(?:&nbsp;| +)?[Cc]\.?([\)\s—–-])', ur'\1s&nbsp;{{versalita|\2}}-{{versalita|\3}}&nbsp;d.&nbsp;C.\4'),

                # Aplicar espacio indivisible en años con especificación de
                # antes o después de Cristo
                (ur'((?:[a-z](?: |&nbsp;)|[—–-] ?|\(|[fmn]\.(?: |&nbsp;))\d{1,6})\s[Aa]\.(?: |&nbsp;)?[Cc]\.([—–-]|\)|\s)(\s*[^\|])', ur'\1&nbsp;a.&nbsp;C.\2\3'),
                (ur'((?:[a-z](?: |&nbsp;)|[—–-] ?|\(|[fmn]\.(?: |&nbsp;))\d{1,6})\s[Dd]\.(?: |&nbsp;)?[Cc]\.([—–-]|\)|\s)(\s*[^\|])', ur'\1&nbsp;d.&nbsp;C.\2\3'),

        # Estandarizar referencias
            # Acercar signos de puntuación a la referencia
            (ur'(</ref>|<ref +name[^>]*?/>) *([\.,:;?!»)])', ur'\1\2'),
            # Acercar referencia a los signos de puntuación
            (ur' *((?:[\.,:;?!"»)])?) *<ref', ur'\1<ref'),
            # Situar referencia tras el signo de puntuación
            (ur' *(<ref>.*?</ref>)((?:[\.,:;?!»])?)', ur'\2\1'),
            (ur' *(<ref +name *=.*?)(</ref>|/>)([\.,:;?!»])?', ur'\3\1\2'),
            # Corregir duplicidades en la puntuación
            (ur'(\w)\.\.<ref', ur'\1.<ref'),
            (ur'(,+|:+|;+)<ref', ur'\1<ref'),

        # Traducir y estandarizar {{ficha de libro}}
        (ur'%s(?:[Ii]nfobox[ _][Bb]ooks?|[Bb]ooks?[ _][Ii]nfobox)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de libro\1'),
        (ur'(%s[Ff]icha[ _]de[ _]libro[^}]*)\b[Ii]mage( *=.*?})' % P_INICIO, ur'\1imagen\2'),
        (ur'(%s[Ff]icha[ _]de[ _]libro[^}]*)\b[Ii]mage_caption( *=.*?})' % P_INICIO, ur'\1pie de imagen\2'),
        (ur'(%s[Ff]icha[ _]de[ _]libro[^}]*)\b[Gg]enre( *=.*?})' % P_INICIO, ur'\1género\2'),
        # Desactivado por https://es.wikipedia.org/?diff=59423057
        ## (ur'({{\s*[Ff]icha[ _]de[ _]libro[^}]*)\b[Nn]ame( *=.*?})', ur'\1título\2'),

        # Pasar a {{documentación}}
        (ur'{{([\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*)([Dd]ocumentation|[Tt]emplate[ _][Dd]oc)([\s_]*[}\|])', ur'{{\1documentación\2'),
        # Pasar a {{navegación}}
        (ur'{{([\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*)[Nn]avbox[ _]subgroup([\s_]*[}\|])', ur'{{\1navegación/subgrupo\2'),
        (ur'{{([\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*)([Nn]avbox|[Nn]avbox[ _]generic|[Nn]avbox[ _]generic[ _]subgroup|[Nn]avigation[Bb]ox|[Pp]lantilla[ _]de[ _]navegación|[Nn]avbox[ _][Aa]rtista[ _][Mm]usical|[Tt]navbar-[Cc]ollapsible|[Nn]avegacion)([\s_]*[}\|])', ur'{{\1navegación\3'),
        # Pasar a {{ficha de artista musical}}
        (ur'%s([Gg]rupo[ _][Mm]usical|[Ii]nfobox[ _][Mm]usical[ _][Aa]rtist|[Ii]nfobox[ _][Aa]rtista[ _][Mm]usical|[Ii]nfobox[ _][Gg]rupo[ _][Mm]usical|[Ff]icha[ _]de[ _][Mm]úsico|[Ff]icha[ _]de[ _][Cc]antante|[Ii]nfobox[ _][Mm]usical[ _][Aa]rtist)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de artista musical\2'),
        # Pasar a {{ficha de taxón}}
        (ur'%s([Tt]axobox[ _][Dd][ée]but|[Ff]icha[ _]de[ _]taxon|[Ff]icha[ _]de[ _][Vv]irus|[Tt]axobox)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de taxón\2'),
        # Pasar a {{ficha de organización}}
        (ur'%s([Ii]nfobox[ _][Cc]ompany|[Ii]nfobox[ _][Ee]mpresa|[Ii]nfobox[ _][Ee]mpresa[ _][Dd]esaparecida|[Ii]nfobox[ _][Oo]rganizaci[óo]n|[Ff]icha[ _]de[ _]ONG|[Ff]icha[ _]de[ _]empresa|[Ff]icha[ _]de[ _]asociaci[óo]n|[Ii]nfobox[ _][Oo]rganization|[Ff]icha[ _]de[ _]Organizaci[óo]n|[Ff]icha[ _]de[ _][Ff][áa]brica)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de organización\2'),
        # Pasar a {{ficha de sencillo}}
        (ur'%s([Ii]nfobox[ _][Ss]ingle)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de sencillo\2'),
        # Pasar a {{ficha de canción}}
        (ur'%s([Cc]anci[óo]n|[Ff]icha[ _]de[ _][Cc]ancion|[Ff]icha[ _]de[ _]Canción)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de canción\2'),
        # Pasar a {{ficha de canal de televisión}}
        (ur'%s([Ii]nfobox[ _][Cc]anal[ _]de[ _]TV|[Tt]elevisora|[Ff]icha[ _]de[ _]televisora|[Ff]icha[ _]de[ _]canal[ _]de[ _]television|[Ii]nfobox[ _]TV[ _]channel)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de canal de televisión\2'),
        # Pasar a {{ficha de persona}}
        (ur'%s([Ii]nfobox[ _][Bb]iograf[íi]a|[Ff]icha[ _]de[ _][Bb]iograf[íi]a|[Ii]nfobox[ _][Pp]ersonalidades)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de persona\2'),
        # Pasar a {{ficha de película}}
        (ur'%s([Ii]nfobox[ _][Pp]el[íi]cula|[Ff]icha[ _]de[ _][Cc]ortometraje|[Ff]icha[ _]de[ _][Pp]elicula)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de película\2'),
        # Pasar a {{ficha de localidad de Japón}}
        (ur'%s([Ii]nfobox[ _][Cc]iudad[ _][Jj]ap[oó]n)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de localidad de Japón\2'),
        # Pasar a {{ficha de localidad de Brasil}}
        (ur'%s([Ii]nfobox[ _][Cc]iudad[ _][Bb]rasil)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de localidad de Brasil\2'),
        # Pasar a {{ficha de localidad de Cuba}}
        (ur'%s([Ii]nfobox[ _][Cc]iudad[ _][Cc]uba)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de localidad de Cuba\2'),
        # Pasar a {{ficha de localidad de Uruguay}}
        (ur'%s([Ii]nfobox[ _][Cc]iudad[ _][Uu]ruguay)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de localidad de Uruguay\2'),
        # Pasar a {{ficha de localidad de Estonia}}
        (ur'%s([Ii]nfobox[ _][Ll]inn)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de localidad de Estonia\2'),
        # Pasar a {{ficha de localidad de Polonia}}
        (ur'%s([Ii]nfobox[ _][Pp]olonia)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de localidad de Polonia\2'),
        # Pasar a {{leyenda}}
        (ur'%s([Ll]egend|[Ll]egend3)([\s_]*[}\|])' % P_INICIO, ur'{{leyenda\2'),
        # Pasar a {{ficha de escultismo}}
        (ur'%s([Ii]nfobox[ _][Ee]scultismomundial)([\s_]*[}\|])' % P_INICIO, ur'{{ficha de escultismo\2'),
        # Pasar a {{etiqueta imagen}} y similares
        (ur'%s[Ii]mage[ _]label[ _]*\|([^}]*)}}' % P_INICIO, ur'{{etiqueta imagen|\1}}'),
        (ur'%s[Ii]mage[ _]label[ _]begin[ _]*\|([^}]*)}}' % P_INICIO, ur'{{etiqueta imagen inicio|\1}}'),
        (ur'%s[Ii]mage[ _]label[ _]small[ _]*\|([^}]*)}}' % P_INICIO, ur'{{etiqueta imagen pequeña|\1}}'),
        (ur'%s[Ii]mage[ _]label[ _]end[ _]*\|([^}]*)}}' % P_INICIO, ur'{{etiqueta imagen fin|\1}}'),
        # Pasar a {{referencias}}
        (ur'%s([Rr]efs|[Uu]nreferenced|[Rr]efimprove|[Uu]nsourced)(\s*[}\|])' % P_INICIO, ur'{{referencias\2'),
        # Pasar a {{copyedit}}
        (ur'%s([Oo]rtografía|[Gg]ramática)(\s*[}\|])' % P_INICIO, ur'{{copyedit\2'),
        # Pasar a {{otros usos}}
        (ur'%s([Oo]trosusos|[Oo]theruses|[Oo]theruses4|[Ss]obre|[Pp]ara)(\s*[}\|])' % P_INICIO, ur'{{otros usos\2'),
        # Pasar a {{distinguir}}
        (ur'%s([Cc]onfusión|[Nn]o\sconfundir)(\s*[}\|])' % P_INICIO, ur'{{distinguir\2'),
        # Pasar a {{desambiguación}}
        (ur'%s([Dd]esambig|[Dd]es|[Dd]esambiguacion|[Dd]isambig)(\s*[}\|])' % P_INICIO, ur'{{desambiguación\2'),
        # Pasar a {{listaref}}
        (ur'%s[Rr]ef(?:erences|list)(\s*[}\|])' % P_INICIO, ur'{{listaref\1'),

        # Estandarizar secciones
            # Álbumes
            (ur'(?i)\n=(=*\s*)([áaà]lbu[mn]e?s)(\s*)=', ur'\n=\1Álbumes\3='),
            # Arquitectura
            (ur'(?i)\n=(=*\s*)(architecture'
                           ur'|arquitect[úu]ra)(\s*)=', ur'\n=\1Arquitectura\3='),
            # Arte
            (ur'(?i)\n=(=*\s*)(arte?)(\s*)=', ur'\n=\1Arte\3='),
            # Bibliografía
            (ur'(?i)\n=(=*\s*)(bibliography'
                           ur'|bibl[íi]?ograf[íiì]as?)(\s*)=', ur'\n=\1Bibliografía\3='),
            # Biografía
            (ur'(?i)\n=(=*\s*)(b[íi][óo]graf[ìií]a'
                           ur'|biography)(\s*)=', ur'\n=\1Biografía\3='),
            # Características
            (ur'(?i)\n=(=*\s*)(car[áaà]cter[íiì]sticas'
                           ur'|features)(\s*)=', ur'\n=\1Características\3='),
            # Carrera
            (ur'(?i)\n=(=*\s*)(carr[ée]ra'
                           ur'|career)(\s*)=', ur'\n=\1Carrera\3='),
            # Carrera artística
            (ur'(?i)\n=(=*\s*)carr[ée]ra(\s+)art[íiì]stica(\s*)=', ur'\n=\1Carrera\2artística\3='),
            (ur'(?i)\n=(=*\s*)(artistic\s+career|career\s+in\s+art)(\s*)=', ur'\n=\1Carrera artística\3='),
            # Crítica
            (ur'(?i)\n=(=*\s*)(cr[íiì]tica)(\s*)=', ur'\n=\1Crítica\3='),
            # Críticas
            (ur'(?i)\n=(=*\s*)(cr[íiì]ticas)(\s*)=', ur'\n=\1Críticas\3='),
            # Cultura
            (ur'(?i)\n=(=*\s*)(cultur[ae])(\s*)=', ur'\n=\1Cultura\3='),
            # Demografía
            (ur'(?i)\n=(=*\s*)(demograf[íiì]a'
                           ur'|demography)(\s*)=', ur'\n=\1Demografía\3='),
            # Descripción
            (ur'(?i)\n=(=*\s*)(description'
                           ur'|descrip[cs]i[óoò]n)(\s*)=', ur'\n=\1Descripción\3='),
            # Discografía
            (ur'(?i)\n=(=*\s*)(discograf[íiì]a'
                           ur'|discography)(\s*)=', ur'\n=\1Discografía\3='),
            # Distribución
            (ur'(?i)\n=(=*\s*)(distribution'
                           ur'|distribu[cs]i[óoò]n)(\s*)=', ur'\n=\1Distribución\3='),
            # Economía
            (ur'(?i)\n=(=*\s*)(econom[íiì]a'
                           ur'|economy)(\s*)=', ur'\n=\1Economía\3='),
            # Educación
            (ur'(?i)\n=(=*\s*)(educa[cst]i[óoò]n)(\s*)=', ur'\n=\1Educación\3='),
            # Enlaces externos
            (ur'(?i)\n=(=*\s*)([bv][íiì]nc[úu]?l[óo]s?\s+e[xs]t[ée]rnos?'
                           ur'|[ée]nla[cs][ée]s?\s+e[xs]t[ée]rnos?'
                           ur'|external\s+links?'
                           ur'|l[íi]gas?\s+e[xs]t[ée]rn[oa]s?'
                           ur'|l[íi]nks?\s+e[xs]t[ée]rn[oa]s?)(\s*)=', ur'\n=\1Enlaces externos\3='),
            # Etimología
            (ur'(?i)\n=(=*\s*)(etimolog[íiì]a'
                           ur'|et[iy]mology)(\s*)=', ur'\n=\1Etimología\3='),
            # Filmografía
            (ur'(?i)\n=(=*\s*)(filmograf[ìií]a'
                           ur'|filmography)(\s*)=', ur'\n=\1Filmografía\3='),
            # Gobierno
            (ur'(?i)\n=(=*\s*)(gobierno'
                           ur'|government)(\s*)=', ur'\n=\1Gobierno\3='),
            # Historia
            (ur'(?i)\n=(=*\s*)(hist[óo]ria'
                           ur'|history)(\s*)=', ur'\n=\1Historia\3='),
            # Infancia
            (ur'(?i)\n=(=*\s*)(inf[áa]n[cs]ia'
                           ur'|childhood)(\s*)=', ur'\n=\1Infancia\3='),
            # Infraestructura
            (ur'(?i)\n=(=*\s*)(infrae?structur[ae])(\s*)=', ur'\n=\1Infraestructura\3='),
            # Localización
            (ur'(?i)\n=(=*\s*)(locali[zs]a[cst]i[óoò]n)(\s*)=', ur'\n=\1Localización\3='),
            # Muerte
            (ur'(?i)\n=(=*\s*)(death'
                           ur'|muerte)(\s*)=', ur'\n=\1Muerte\3='),
            # Música
            (ur'(?i)\n=(=*\s*)(m[úuù]sica'
                           ur'|music)(\s*)=', ur'\n=\1Música\3='),
            # Notas y referencias
            (ur'(?i)\n=(=*\s*)(notas\s+y\s+refer[ée]n[cs]ias'
                           ur'|notes\s+and\s+references'
                           ur'|refer[ée]n[cs]ias\s+y\s+notas'
                           ur'|references\s+and\s+notes)(\s*)=', ur'\n=\1Notas y referencias\3='),
            # Obra
            (ur'(?i)\n=(=*\s*)(obra)(\s*)=', ur'\n=\1Obra\3='),
            # Población
            (ur'(?i)\n=(=*\s*)(pobla[cs]i[óoò]n'
                           ur'|population)(\s*)=', ur'\n=\1Población\3='),
            # Premios
            (ur'(?i)\n=(=*\s*)(pr[ée]mios'
                           ur'|awards)(\s*)=', ur'\n=\1Premios\3='),
            # Premios y reconocimientos
            (ur'(?i)\n=(=*\s*)(pr[ée]mios\s+y\s+recono[cs]imi[ée]ntos'
                           ur'|awards\s+and\s+honors)(\s*)=', ur'\n=\1Premios y reconocimientos\3='),
            # Referencias
            (ur'(?i)\n=(=*\s*)(refer[éèe]n[cs]ias'
                           ur'|references?'
                           ur'|einzelnachweise)(\s*)=', ur'\n=\1Referencias\3='),
            # Ubicación
            (ur'(?i)\n=(=*\s*)(ubica[cst]i[óoò]n)(\s*)=', ur'\n=\1Ubicación\3='),
            # Últimos años
            (ur'(?i)\n=(=*\s*)(last +years'
                           ur'|[úuù]ltimos +años)(\s*)=', ur'\n=\1Últimos años\3='),
            # Véase también
            (ur'(?i)\n=(=*\s*)(see\s+also'
                           ur'|[vb]er\s+t[áa][nm][bv]i[éeè]n'
                           ur'|m[íiì]r[ea](?:se)?\s+ta[nm][vb]?i[éeè]n'
                           ur'|[vb][éeè]a?n?[cs]e\s+t[aá][nm][vb]i[éeè]n'
                           ur'|v[éeè]a\s+ta[nm][vb]i[éeè]n'
                           ur'|art[íiì]cu?los?\s+[Rr]elacion[áa]dos?)(\s*)=', ur'\n=\1Véase también\3='),
            
    ],
    'exceptions': {
        'inside-tags': [
            'blockquote',
            'categorytree',
            'charinsert',
            'comment',
            'dynamicpagelist',
            'gallery',
            'hiero',
            'hyperlink',
            'imagemap',
            'indicator',
            'inputbox',
            'invoke',
            'math',
            'nowiki',
            'pagelist',
            'pagequality',
            'pages',
            'poem',
            'pre',
            'property',
            'score',
            'section',
            'source',
            'syntaxhighlight',
            'templatedata',
            'timeline',
        ],
        'inside': [
            # Enlaces con números en el título enlazado
            ur'\[\[[^\]\|]*?\d+[^\]\|]*?[\]\|]',
            # Expresiones literales entre comillas
            ur'«.*?»',
            ur'\s"[^"]+"[\s\.,;:]',
            # Contenido de citas
            (ur'%s([Cc]ita'
               ur'|[Qq]uote'
               ur'|[Cc]quote'
               ur'|[Qq]uotation'
               ur'|[Zz]itat'
               ur')[\s_]*\|.+?}}') % P_INICIO,
            ur'{{[^}]+?\|[\s_]*(cita|quote|quotation)[\s_]*=.+?(}}|\|)',
            # Títulos, por falsos positivos
            ur'\|\s*(title|t[íi]tulo)\s*=\s*[^\]\|]*?[\]\|]',
            # Minúsculas inciertas en meses
            (ur'(?i)(acuerdo'
                 ur'|decreto'
                 ur'|ley'
                 ur'|norma(tiva)?'
                 ur'|[óo]rden'
                 ur'|procedimiento'
                 ur'|resoluci[óo]n'
                 ur') +del? +\d\d? +del? +\S\S'),
            # Parámetros de {{cita web}} inseguros
            (ur'%s[Rr]ef[-](internet|web)[^}]*(?:[Aa]lias\d?'
                                             ur'|[Aa]pellido\d'
                                             ur'|[Aa]utor\d'
                                             ur'|[Cc]ap[íi]tulo'
                                             ur'|[Cc]ontribuci[óo]n'
                                             ur'|[Ff]amilia\d?'
                                             ur'|[Ii]niciales\d?'
                                             ur'|[Ii][Ss][Bb][Nn]'
                                             ur'|[Nn]ombre\d'
                                             ur'|[Nn][úu]mero'
                                             ur'|[Pp]eri[óo]dico'
                                             ur'|[Rr]ef'
                                             ur'|[Rr]evista'
                                             ur'|[Vv][íi]nculo ?autor\d'
                                             ur')\s*=.*?[|}]') % P_INICIO,
            # No editar si el artículo contiene determinadas plantillas
                # Artículos cuya edición por bots queda prohibida según
                # [[w:es:WP:PBOT#R9.3]]
                ur'.*%s[Nn]obots[\s_]*[|}].*' % P_INICIO,
                # Artículos en desarrollo activo
                ur'.*%s[Ee]n[ _]?uso[\s_]*[|}].*' % P_INICIO,
                # Plantillas de mantenimiento
                ## Excepciones deshabilitadas por sobrecarga --abián, 6 feb 2015
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*autotrad[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*artículo[ _]infraesbozo[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*autopromoción[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*aviso[ _]borrar[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*bloqueo[ _]permanente[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*borrar[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cdb[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*contextualizar[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*copyright[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*copyvio[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*d[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*db[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*delete[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*destruir[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*eliminar[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*fp[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*fuente[ _]?primaria[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*huggle[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*infraesbozo[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*irrelevante[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*plagio[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*posible[ _]copyvio[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*promocional[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*propb[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*propb[ _]fecha[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*reducido[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*robotdestruir[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*sin[ _]?relevancia[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*speedy[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*sra[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*t[íi]tere[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*traducción[ _]automática[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*traducción[ _]incomprensible[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*usuario[ _]expulsado[\s_]*[|}].*',
                ##ur'(?i).*{{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*usuario[ _]títere[|}].*[\s_]*[|}].*',
            # Preservar integridad de los puntos suspensivos siempre
            ur'\.\.\.',
            # Con referencias como parámetros, evitar cambios cosméticos
            ur'[^=]=\s*<ref',
            # Con referencias como celdas, evitar cambios cosméticos
            ur'\|\s*<ref', # https://es.wikipedia.org/?diff=80029650
            # Categorías
            #  Se hace "avaricioso" por tratarse del final del artículo, donde
            #  no se efectuarán más modificaciones
            ur'(?i)\[\[[\s_]*categor[íiy]a?\s*:.*\]',
        ],
    }
}
# </nowiki>
# ============================================================================ #


# ============================================================================ #
#
#   +-------------------------+  https://es.wikipedia.org/wiki/User:Invadibot
#   |  Invadibot,  eswiki-21  |  https://meta.wikimedia.org/wiki/User:Invadibot
#   +-------------------------+  http://davidabian.com/invadibot/
#
#   [es] Expresiones regulares para corregir el formato de los mensajes
#        publicados en el Libro de visitas de Wikipedia en español y sus
#        archivos y prevenir el spam.
#
# <nowiki>
fixes['inva-wp-es-librovisitas'] = {
     'nocase': False,
     'recursive': True,
     'regex': True,
     'msg': {
          'es': u'Bot: [[m:User:Invadibot/scope#eswiki|21]] - Correcciones de formato y protección antispam',
          'test': u'Bot: Testing',
     },
     'replacements': [
          # retirar líneas en blanco innecesarias
          (ur'\r\n\r(\n\r)+\n', ur'\n\n'),
          # retirar espacios a principio de línea (<pre>)
          (ur'\n[ \t]+(\S)', ur'\n\1'),
          # impedir secciones de nivel 1
          (ur'\n= *([^=]+) *=+\r\n', ur'\n== \1 ==\n'),
          # protección antispam con {{@}}
          (ur'(\w\w)@(\w+\.\w)', ur'\1{{@}}\2'),
          # retirar comentarios orientativos de la precarga
          (ur'\n<!-- ?Abajo es[^\n]*?no lo borres\.? *-->\r\n', ur'\n'),
          (ur'\n<!-- ?Aqu[^\n]*?las instrucciones de arriba\.? *-->\r\n', ur'\n'),
          # retirar firmas repetidas
          (ur'(--\[\[(?:Especial:Contribu|Usuario:|User:)[^\]]*?\]\] \(\[\[(?:Usuario[_ ][Dd]iscu|User[_ ][Tt]alk)[^\]]*?\]\]\) \d\d?:\d\d \d\d? \S{3,4} \d{4} \((UTC|GMT)\))\1+', ur'\1'),
     ],
     'exceptions': {
         'inside-tags': [
               'categorytree',
               'comment',
               'charinsert',
               'dynamicpagelist',
               'gallery',
               'hiero',
               'imagemap',
               'inputbox',
               'invoke',
               'math',
               ## 'nowiki',
               'pagelist',
               'pagequality',
               'pages',
               'poem',
               ## 'pre',
               'property',
               'score',
               ## 'section',
               'source',
               'syntaxhighlight',
               'templatedata',
               'timeline',
          ]
     }
}
# </nowiki>
# ============================================================================ #
