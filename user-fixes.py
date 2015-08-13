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
        (ur'(?i){{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*invadibot[^}]*?}}\s*(.)', ur'\1'),

        # Pasar a {{cita libro}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]it[ae][ _]*book([\s_]*[}\|])', ur'{{cita libro\1'),
        # Pasar a {{cita noticia}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]it[ae][\s_]*[Nn]ews([\s_]*[}\|])', ur'{{cita noticia\1'),
        # Pasar a {{cita publicación}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*(?:[Cc]it[ae]r?[ _]*journal|[Cc]it(?:ar|e)[ _]*publicaci[óo]n?|[Cc]itar?[ _]*revista|[Rr]ef[- ]publicaci[óo]n?)([\s_]*[}\|])', ur'{{cita publicación\1'),
        # Pasar a {{cita vídeo}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*(?:[Cc]it[ae]r?[ _]*video|[Cc]it(?:ar|e)[ _]*vídeo|[Cc]it[ae]r?[ _]*[Aa][Vv][ _]*[Mm]edia)([\s_]*[}\|])', ur'{{cita vídeo\1'),
        # Pasar a {{cita web}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*(?:[Cc]ite[ _-]?web(?:site)?|[Cc]itar[ _]web|[Ww]eb[ _-]cite|[Ll]ien[ _-]web|[Rr]ef[ _-](?:internet|web))([\s_]*[}\|])', ur'{{cita web\1'),
        
        # Traducción y estandarización indiscriminadas de parámetros para citas
        # libro, noticia, publicación y web
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Aa]ccessdate(\s*=.*?})', ur'\1fechaacceso\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Aa]ccessmonth(\s*=.*?})', ur'\1mesacceso\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Aa]ccessmonthday(\s*=.*?})', ur'\1mesacceso\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Aa]cces+o(\s*=.*?})', ur'\1fechaacceso\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Aa]ccessyear(\s*=.*?})', ur'\1añoacceso\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Aa]ny(\s*=.*?})', ur'\1año\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Aa]rchivedate(\s*=.*?})', ur'\1fechaarchivo\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Aa]rchiveurl(\s*=.*?})', ur'\1urlarchivo\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Aa]rxiudata(\s*=.*?})', ur'\1fechaarchivo\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Aa]rxiuurl(\s*=.*?})', ur'\1urlarchivo\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Aa]uthor(\d{0,2}\s*=.*?})', ur'\1autor\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Aa]uthorlink(\d{0,2}\s*=.*?})', ur'\1enlaceautor\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Aa]utorenllaç(\d{0,2}\s*=.*?})', ur'\1enlaceautor\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Cc]apítol(\s*=.*?})', ur'\1capítulo\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Cc]hapter(\s*=.*?})', ur'\1capítulo\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Cc]hapterurl(\s*=.*?})', ur'\1urlcapítulo\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Cc]itació(\s*=.*?})', ur'\1cita\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Cc]ittà(\s*=.*?})', ur'\1ubicación\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Cc]oauthors(\s*=.*?})', ur'\1coautores\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Cc]oautors(\s*=.*?})', ur'\1coautores\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Cc]ol·lecció(\s*=.*?})', ur'\1obra\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Cc]ognom(\d{0,2}\s*=.*?})', ur'\1apellido\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Cc]onsulta(\s*=.*?})', ur'\1fechaacceso\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Dd]ate(\s*=.*?})', ur'\1fecha\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ee]dici[óo](\s*=.*?})', ur'\1edición\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ee]dition(\s*=.*?})', ur'\1edición\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ee]nllaçautor(\d{0,2}\s*=.*?})', ur'\1enlaceautor\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ff]echa[ _]de[ _]acceso(\s*=.*?})', ur'\1fechaacceso\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ff]echaaacceso(\s*=.*?})', ur'\1fechaacceso\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ff]irst(\s*=.*?})', ur'\1nombre\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ff]ormat(\s*=.*?})', ur'\1formato\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ii][Dd](\s*=.*?})', ur'\1id\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ii][Ss][Bb][Nn](\s*=.*?})', ur'\1isbn\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ii]ssue(\s*=.*?})', ur'\1número\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Jj]ournal(\s*=.*?})', ur'\1publicación\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ll]anguage(\s*=.*?})', ur'\1idioma\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ll]ast(\s*=.*?})', ur'\1apellido\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ll]aydate(\s*=.*?})', ur'\1fechaprofano\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ll]aysource(\s*=.*?})', ur'\1fuenteprofano\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ll]aysummary(\s*=.*?})', ur'\1resumenprofano\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ll]lengua(\s*=.*?})', ur'\1idioma\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ll]loc(\s*=.*?})', ur'\1ubicación\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ll]ocation(\s*=.*?})', ur'\1ubicación\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ll]ugar(\s*=.*?})', ur'\1ubicación\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Mm]onth(\s*=.*?})', ur'\1mes\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Nn]om(\d{0,2}\s*=.*?})', ur'\1nombre\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Oo]thers(\s*=.*?})', ur'\1otros\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Pp]age(\s*=.*?})', ur'\1página\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Pp]ages(\s*=.*?})', ur'\1páginas\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Pp]àgina(\s*=.*?})', ur'\1página\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Pp][aà]gines(\s*=.*?})', ur'\1páginas\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Pp]ublicaci[óo](\s*=.*?})', ur'\1publicación\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Pp]ublisher(\s*=.*?})', ur'\1editorial\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Qq]uote(\s*=.*?})', ur'\1cita\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Tt]itle(\s*=.*?})', ur'\1título\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Tt][íi]tol(\s*=.*?})', ur'\1título\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Uu]bicacion(\s*=.*?})', ur'\1ubicación\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Uu]rlcapítol(\s*=.*?})', ur'\1urlcapítulo\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Vv][ií]ncu?lo[ _]autora?(\s*=.*?})', ur'\1enlaceautor\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Vv]olum(\s*=.*?})', ur'\1volumen\2'), #ca
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Vv]olume(\s*=.*?})', ur'\1volumen\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Vv]olúmen(\s*=.*?})', ur'\1volumen\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Vv]olumem(\s*=.*?})', ur'\1volumen\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Ww]ork(\s*=.*?})', ur'\1obra\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)[Yy]ear(\s*=.*?})', ur'\1año\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*)U(?:RL|rl)(\s*=.*?})', ur'\1url\2'),

        # Traducir ubicaciones (en orden alfabético en español)
        (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*ubicación\s*=\s*)(?:bagh?dad)(\s*[}\|])', ur'\1Bagdad\2'),
        (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*ubicación\s*=\s*)(?:[ei]sta[mn]bul)(\s*[}\|])', ur'\1Estambul\2'),
        (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*ubicación\s*=\s*)(?:londres|london)(\s*[}\|])', ur'\1Londres\2'),
        (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*ubicación\s*=\s*)(?:m[éeè][jx]ico,? ?d\.? ?f\.?|mexico city)(\s*[}\|])', ur'\1México,&nbsp;D.&nbsp;F.\2'),
        (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*ubicación\s*=\s*)(?:mosc[úuù]|moscow|moskva)(\s*[}\|])', ur'\1Moscú\2'),
        (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*ubicación\s*=\s*)(?:nanjing|nank[íiì]ng?)(\s*[}\|])', ur'\1Nankín\2'),
        (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*ubicación\s*=\s*)(?:nueva delh?i|new delhi)(\s*[}\|])', ur'\1Nueva&nbsp;Delhi\2'),
        (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*ubicación\s*=\s*)(?:nue[bv]a york?|new york(?: city)?)(\s*[}\|])', ur'\1Nueva&nbsp;York\2'),
        (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*ubicación\s*=\s*)(?:beijing|pek[íiì]ng?)(\s*[}\|])', ur'\1Pekín\2'),
        (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*ubicación\s*=\s*)(?:seo?[úuù]l)(\s*[}\|])', ur'\1Seúl\2'),
        (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*ubicación\s*=\s*)(?:sevill[ae])(\s*[}\|])', ur'\1Sevilla\2'),
        (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*ubicación\s*=\s*)(?:sh?angh?[áaà]i)(\s*[}\|])', ur'\1Shanghái\2'),
        (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*ubicación\s*=\s*)(?:tehe?r[áaà]n)(\s*[}\|])', ur'\1Teherán\2'),
        (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*ubicación\s*=\s*)(?:tok[iy]o)(\s*[}\|])', ur'\1Tokio\2'),

        # Traducir idiomas (en orden alfabético en español)
            # Traducciones de "alemán" al español
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)german(\s*[}\|])', ur'\1alemán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)alem[ãa]o(\s*[}\|])', ur'\1alemán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)all?emande?(\s*[}\|])', ur'\1alemán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)all?em[áa]ny?(\s*[}\|])', ur'\1alemán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)de[iu]tsche?(\s*[}\|])', ur'\1alemán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)duits(\s*[}\|])', ur'\1alemán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)gearm[áa]inis(\s*[}\|])', ur'\1alemán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)germanaj(\s*[}\|])', ur'\1alemán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)tedesco(\s*[}\|])', ur'\1alemán\2'),
                # En inglés con enlace
                (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)\[\[\s*german[ _]language\s*\|\s*german\s*\]\](\s*[}\|])', ur'\1[[Idioma alemán|alemán]]\2'),

            # Traducciones de "catalán" al español
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)catal[ãáaà]o?(\s*[}\|])', ur'\1catalán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)catal[áaà]n[aeio]?(\s*[}\|])', ur'\1catalán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)catal[óo]inis(\s*[}\|])', ur'\1catalán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)catalaanse?(\s*[}\|])', ur'\1catalán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)katalana?(\s*[}\|])', ur'\1catalán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)katalanaren(\s*[}\|])', ur'\1catalán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)katalanische?n?(\s*[}\|])', ur'\1catalán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)katalanska(\s*[}\|])', ur'\1catalán\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)katalunaj?(\s*[}\|])', ur'\1catalán\2'),
                # En inglés con enlace
                (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)\[\[\s*catalan[ _]language\s*\|\s*catalan\s*\]\](\s*[}\|])', ur'\1[[Idioma catalán|catalán]]\2'),

            # Traducciones de "español" al español
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)castell[àa](\s*[}\|])', ur'\1español\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)espagnole?(\s*[}\|])', ur'\1español\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)espainiako(\s*[}\|])', ur'\1español\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)espan[hiy]?ol(\s*[}\|])', ur'\1español\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)españ[óo]l(\s*[}\|])', ur'\1español\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)hispan[ao](\s*[}\|])', ur'\1español\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)sp[áaà]innis(\s*[}\|])', ur'\1español\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)spaans(\s*[}\|])', ur'\1español\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)spagnolo(\s*[}\|])', ur'\1español\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)spanische?n?(\s*[}\|])', ur'\1español\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)spanish(\s*[}\|])', ur'\1español\2'),
                # En inglés con enlace
                (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)\[\[\s*spanish[ _]language\s*\|\s*spanish\s*\]\](\s*[}\|])', ur'\1[[Idioma español|español]]\2'),

            # Traducciones de "francés" al español
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)french(\s*[}\|])', ur'\1francés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)ffrangeg(\s*[}\|])', ur'\1francés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)fraincis(\s*[}\|])', ur'\1francés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)fran[çc]aise?(\s*[}\|])', ur'\1francés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)franc[éêèe]se?(\s*[}\|])', ur'\1francés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)francaj(\s*[}\|])', ur'\1francés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)frans(\s*[}\|])', ur'\1francés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)franska(\s*[}\|])', ur'\1francés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)frantsesa?(\s*[}\|])', ur'\1francés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)franz[öo]sische?(\s*[}\|])', ur'\1francés\2'),
                # En inglés con enlace
                (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)\[\[\s*french[ _]language\s*\|\s*french\s*\]\](\s*[}\|])', ur'\1[[Idioma francés|francés]]\2'),
            
            # Traducciones de "inglés" al español
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)angl[éèe]s(\s*[}\|])', ur'\1inglés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)anglais(\s*[}\|])', ur'\1inglés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)anglaj(\s*[}\|])', ur'\1inglés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)anglicus(\s*[}\|])', ur'\1inglés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)b[ée]arla(\s*[}\|])', ur'\1inglés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)engels(\s*[}\|])', ur'\1inglés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)engelska(\s*[}\|])', ur'\1inglés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)englez(\s*[}\|])', ur'\1inglés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)englische?(\s*[}\|])', ur'\1inglés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)english(\s*[}\|])', ur'\1inglés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)ingl[éêèe]se?(\s*[}\|])', ur'\1inglés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)saesneg(\s*[}\|])', ur'\1inglés\2'),
                # En inglés con enlace
                (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)\[\[\s*english[ _]language\s*\|\s*english\s*\]\](\s*[}\|])', ur'\1[[Idioma inglés|inglés]]\2'),
            
            # Traducciones de "italiano" al español
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)iodáilis(\s*[}\|])', ur'\1italiano\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)ital[ao]j(\s*[}\|])', ur'\1italiano\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)itali[áaà](\s*[}\|])', ur'\1italiano\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)itali[ae]no?(\s*[}\|])', ur'\1italiano\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)italiaa?ns(\s*[}\|])', ur'\1italiano\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)italienische?(\s*[}\|])', ur'\1italiano\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)italiensk(\s*[}\|])', ur'\1italiano\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)taljan(\s*[}\|])', ur'\1italiano\2'),
                # En inglés con enlace
                (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)\[\[\s*italian[ _]language\s*\|\s*italian\s*\]\](\s*[}\|])', ur'\1[[Idioma italiano|italiano]]\2'),
            
            # Traducciones de "neerlandés" al español
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)dutch(\s*[}\|])', ur'\1neerlandés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)nederlaa?nds?(\s*[}\|])', ur'\1neerlandés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)niederl[aä]ndische?(\s*[}\|])', ur'\1neerlandés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)niderlandzki(\s*[}\|])', ur'\1neerlandés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)n[éeè][éeè]?rland[aéeè]i?[sz][aăe]?(\s*[}\|])', ur'\1neerlandés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)olandese?(\s*[}\|])', ur'\1neerlandés\2'),
                # En inglés con enlace
                (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)\[\[\s*dutch[ _]language\s*\|\s*dutch\s*\]\](\s*[}\|])', ur'\1[[Idioma neerlandés|neerlandés]]\2'),

            # Traducciones de "portugués" al español
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)portugu?[éêèe]e?s[ae]?(\s*[}\|])', ur'\1portugués\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)portaing[ée]ilis(\s*[}\|])', ur'\1portugués\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)portogh[êéèe]se?(\s*[}\|])', ur'\1portugués\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)portugaise?(\s*[}\|])', ur'\1portugués\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)portugala(\s*[}\|])', ur'\1portugués\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)portugiesische?(\s*[}\|])', ur'\1portugués\2'),
                # En inglés con enlace
                (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)\[\[\s*portuguese[ _]language\s*\|\s*portuguese\s*\]\](\s*[}\|])', ur'\1[[Idioma portugués|portugués]]\2'),

            # Traducciones de "ruso" al español
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)rusa?(\s*[}\|])', ur'\1ruso\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)errusiera(\s*[}\|])', ur'\1ruso\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)rúisis(\s*[}\|])', ur'\1ruso\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)russ[eo](\s*[}\|])', ur'\1ruso\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)russiann?e?(\s*[}\|])', ur'\1ruso\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)russische?n?(\s*[}\|])', ur'\1ruso\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)russkaya(\s*[}\|])', ur'\1ruso\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)russkiy(\s*[}\|])', ur'\1ruso\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)rwsia(\s*[}\|])', ur'\1ruso\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)ryska(\s*[}\|])', ur'\1ruso\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)русская(\s*[}\|])', ur'\1ruso\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)русский(\s*[}\|])', ur'\1ruso\2'),
                # En inglés con enlace
                (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)\[\[\s*russian[ _]language\s*\|\s*russian\s*\]\](\s*[}\|])', ur'\1[[Idioma ruso|ruso]]\2'),

            # Traducciones de "sueco" al español
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)schwedische?n?(\s*[}\|])', ur'\1sueco\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)su[ée]co?(\s*[}\|])', ur'\1sueco\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)su[éeè]doise?(\s*[}\|])', ur'\1sueco\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)sualainnis(\s*[}\|])', ur'\1sueco\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)suediako(\s*[}\|])', ur'\1sueco\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)suediarrak?(\s*[}\|])', ur'\1sueco\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)sved[ao]j?(\s*[}\|])', ur'\1sueco\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)svedese(\s*[}\|])', ur'\1sueco\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)svensk[ae]?(\s*[}\|])', ur'\1sueco\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)swed[ei]g(\s*[}\|])', ur'\1sueco\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)swedish(\s*[}\|])', ur'\1sueco\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)swedish(\s*[}\|])', ur'\1sueco\2'),
                # En inglés con enlace
                (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)\[\[\s*swedish[ _]language\s*\|\s*swedish\s*\]\](\s*[}\|])', ur'\1[[Idioma sueco|sueco]]\2'),

            # Más traducciones, solo del inglés al español, y estandarización
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)bengal[íi](\s*[}\|])', ur'\1bengalí\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)chin(?:ese|o)(\s*[}\|])', ur'\1chino\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)[ck]ore[áa]no?(\s*[}\|])', ur'\1coreano\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)jap(?:anese|on[éeè]s)(\s*[}\|])', ur'\1japonés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)javan[éeè]se?(\s*[}\|])', ur'\1javanés\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)mandar[íiì]n(\s*[}\|])', ur'\1mandarín\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)marath?[íiì](\s*[}\|])', ur'\1maratí\2'),
            (ur'(?i)({{[\s_]*(?:plantilla[\s_]*:|template[\s_]*:)?[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*idioma\s*=\s*)telug[úuù](\s*[}\|])', ur'\1telugú\2'),

        # Estandarizar y traducir fechas al español
            # En plantillas de citas
                # AAAA[-/\\\.]MM[-/\\\.]DD → DD-MM-AAAA
                (ur'({{[\s_]*[Cc]ita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)([12]\d\d\d)[-/\\\.](\d\d?)[-/\\\.](\d\d?)(\s*[}\|])', ur'\1\4-\3-\2\5'),

                # Estandarizar y traducir meses aislados
                #  Ejemplo: {{cita web|mes=January}} → {{cita web|mes=enero}}
                #  Idiomas garantizados: es, en, fr, sv
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*\bmes\s*=\s*)(?:en[éeè]ro|januar[iy]|janvier)', ur'\1enero'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*\bmes\s*=\s*)(?:febr[éeè]ro|februar[iy]|f[éeè]vrier)', ur'\1febrero'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*\bmes\s*=\s*)(?:m[áaà]rzo|march|mars)', ur'\1marzo'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*\bmes\s*=\s*)(?:abr[íiì]l|april|avril)', ur'\1abril'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*\bmes\s*=\s*)(?:m[áaà]yo|ma[ijy])', ur'\1mayo'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*\bmes\s*=\s*)(?:j[úuù]nio|jun[ei]|juin)', ur'\1junio'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*\bmes\s*=\s*)(?:j[úuù]lio|jul[iy]|juillet)', ur'\1julio'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*\bmes\s*=\s*)(?:ag[óoò]sto|augusti?|ao[ûu]t)', ur'\1agosto'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*\bmes\s*=\s*)(?:septi[éeè]mbre|september|septembre)', ur'\1septiembre'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*\bmes\s*=\s*)(?:oct[úuù]bre|o[ck]tober|octobre)', ur'\1octubre'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*\bmes\s*=\s*)(?:novi[éeè]mbre|november|novembre)', ur'\1noviembre'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*\bmes\s*=\s*)(?:dici[éeè]mbre|december|d[éeè]cembre)', ur'\1diciembre'),

                # Estandarizar y traducir fechas con palabras
                #  Idiomas garantizados: es, en, fr, sv
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:en[éeè]ro|januar[iy]|janvier)\b', ur'\1 de enero'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:febr[éeè]ro|februar[iy]|f[éeè]vrier)\b', ur'\1 de febrero'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:m[áaà]rzo|march|mars)\b', ur'\1 de marzo'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:abr[íiì]l|april|avril)\b', ur'\1 de abril'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:m[áaà]yo|ma[ijy])\b', ur'\1 de mayo'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:j[úuù]nio|jun[ei]|juin)\b', ur'\1 de junio'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:j[úuù]lio|jul[iy]|juillet)\b', ur'\1 de julio'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:ag[óoò]sto|augusti?|ao[ûu]t)\b', ur'\1 de agosto'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:septi[éeè]mbre|september|septembre)\b', ur'\1 de septiembre'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:oct[úuù]bre|o[ck]tober|octobre)\b', ur'\1 de octubre'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:novi[éeè]mbre|november|novembre)\b', ur'\1 de noviembre'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)[\s\-/](?:dici[éeè]mbre|december|d[éeè]cembre)\b', ur'\1 de diciembre'),

                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:en[éeè](?:ro)?|jan(?:uar[iy])?|janvier)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1 de enero de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:feb(?:r[éeè]ro)?|februar[iy]|f[éeè]v(?:rier)?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1 de febrero de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:m[áaà]r(?:zo)?|march|mars)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1 de marzo de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:abr(?:[íiì]l)?|apr(?:il)?|avr(?:il)?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1 de abril de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:m[áaà]yo?|ma[ijy])[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1 de mayo de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:j[úuù]n(?:io)?|jun[ei]|juin)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1 de junio de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:j[úuù]l(?:io)?|jul[iy]|juil(?:let)?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1 de julio de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:ag[óoò](?:sto)?|aug(?:usti?)?|ao[ûu]t)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1 de agosto de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:sept?(?:i[éeè]mbre)?|september|septembre)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1 de septiembre de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:oct[úuù]bre|o[ck]t(?:ober)?|octobre)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1 de octubre de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:nov(?:i[éeè]mbre)?|november|novembre)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1 de noviembre de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*\d\d?)(?:[\s\-/]| de )(?:dic(?:i[éeè]mbre)?|december|d[éeè]c(?:embre)?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1 de diciembre de \2\3'),

                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:en[éeè]ro|januar[iy]|janvier)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1enero de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:febr[éeè]ro|februar[iy]|f[éeè]vrier)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1febrero de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:m[áaà]rzo|march|mars)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1marzo de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:abr[íiì]l|april|avril)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1abril de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:m[áaà]yo|ma[ijy])[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1mayo de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:j[úuù]nio|jun[ei]|juin)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1junio de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:j[úuù]lio|jul[iy]|juillet)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1julio de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:ag[óoò]sto|augusti?|ao[ûu]t)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1agosto de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:septi[éeè]mbre|september|septembre)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1septiembre de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:oct[úuù]bre|o[ck]tober|octobre)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1octubre de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:novi[éeè]mbre|november|novembre)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1noviembre de \2\3'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:dici[éeè]mbre|december|d[éeè]cembre)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1diciembre de \2\3'),

                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:en[éeè]ro|januar[iy]|janvier)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1\2 de enero de \3\4'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:febr[éeè]ro|februar[iy]|f[éeè]vrier)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1\2 de febrero de \3\4'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:m[áaà]rzo|march|mars)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1\2 de marzo de \3\4'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:abr[íiì]l|april|avril)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1\2 de abril de \3\4'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:m[áaà]yo|ma[ijy])[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1\2 de mayo de \3\4'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:j[úuù]nio|jun[ei]|juin)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1\2 de junio de \3\4'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:j[úuù]lio|jul[iy]|juillet)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1\2 de julio de \3\4'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:ag[óoò]sto|augusti?|ao[ûu]t)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1\2 de agosto de \3\4'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:septi[éeè]mbre|september|septembre)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1\2 de septiembre de \3\4'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:oct[úuù]bre|o[ck]tober|octobre)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1\2 de octubre de \3\4'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:novi[éeè]mbre|november|novembre)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1\2 de noviembre de \3\4'),
                (ur'(?i)({{[\s_]*cita[ _](?:libro|noticia|publicación|web)[^}]*?\|\s*(?:fecha|fechaacceso|fechaarchivo)\s*=\s*)(?:dici[éeè]mbre|december|d[éeè]cembre)[\s\-/](\d\d?)[\s\-/,]+([12]\d\d\d)(\s*[}\|])', ur'\1\2 de diciembre de \3\4'),

            # En cualquier ámbito
                # Aplicar minúscula inicial al mes, retirar artículo al año y
                # suprimir posible sustantivo "día" en años posteriores al 99
                #  Ejemplo: día 12 de Marzo del 1456 → 12 de marzo de 1456
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Ee]nero\s+del?\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\2enero de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Ff]ebrero\s+del?\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\2febrero de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Mm]arzo\s+del?\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\2marzo de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Aa]bril\s+del?\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\2abril de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Mm]ayo\s+del?\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\2mayo de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Jj]unio\s+del?\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\2junio de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Jj]ulio\s+del?\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\2julio de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Aa]gosto\s+del?\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\2agosto de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Ss]eptiembre\s+del?\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\2septiembre de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Ss]etiembre\s+del?\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\2setiembre de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Oo]ctubre\s+del?\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\2octubre de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Nn]oviembre\s+del?\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\2noviembre de \3\4'),
                (ur'([Dd][íi]a\s+)?(\d\d?\s+de\s+)[Dd]iciembre\s+del?\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\2diciembre de \3\4'),

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
                (ur'([^\d])0(\d\s+de\s+)enero\s+de\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\1\2enero de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)febrero\s+de\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\1\2febrero de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)marzo\s+de\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\1\2marzo de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)abril\s+de\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\1\2abril de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)mayo\s+de\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\1\2mayo de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)junio\s+de\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\1\2junio de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)julio\s+de\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\1\2julio de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)agosto\s+de\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\1\2agosto de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)septiembre\s+de\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\1\2septiembre de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)setiembre\s+de\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\1\2setiembre de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)octubre\s+de\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\1\2octubre de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)noviembre\s+de\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\1\2noviembre de \3\4'),
                (ur'([^\d])0(\d\s+de\s+)diciembre\s+de\s+(\[\[)?\s?(\d\d\d\d?[^\d])', ur'\1\2diciembre de \3\4'),

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
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*(?:[Ii]nfobox[ _][Bb]ooks?|[Bb]ooks?[ _][Ii]nfobox)([\s_]*[}\|])', ur'{{ficha de libro\1'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Ff]icha[ _]de[ _]libro[^}]*)\b[Ii]mage( *=.*?})', ur'\1imagen\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Ff]icha[ _]de[ _]libro[^}]*)\b[Ii]mage_caption( *=.*?})', ur'\1pie de imagen\2'),
        (ur'({{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Ff]icha[ _]de[ _]libro[^}]*)\b[Gg]enre( *=.*?})', ur'\1género\2'),
        # Desactivado por https://es.wikipedia.org/?diff=59423057
        ## (ur'({{\s*[Ff]icha[ _]de[ _]libro[^}]*)\b[Nn]ame( *=.*?})', ur'\1título\2'),

        # Pasar a {{documentación}}
        (ur'{{([\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*)([Dd]ocumentation|[Tt]emplate[ _][Dd]oc)([\s_]*[}\|])', ur'{{\1documentación\2'),
        # Pasar a {{navegación}}
        (ur'{{([\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*)[Nn]avbox[ _]subgroup([\s_]*[}\|])', ur'{{\1navegación/subgrupo\2'),
        (ur'{{([\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*)([Nn]avbox|[Nn]avbox[ _]generic|[Nn]avbox[ _]generic[ _]subgroup|[Nn]avigation[Bb]ox|[Pp]lantilla[ _]de[ _]navegación|[Nn]avbox[ _][Aa]rtista[ _][Mm]usical|[Tt]navbar-[Cc]ollapsible|[Nn]avegacion)([\s_]*[}\|])', ur'{{\1navegación\3'),
        # Pasar a {{ficha de artista musical}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Gg]rupo[ _][Mm]usical|[Ii]nfobox[ _][Mm]usical[ _][Aa]rtist|[Ii]nfobox[ _][Aa]rtista[ _][Mm]usical|[Ii]nfobox[ _][Gg]rupo[ _][Mm]usical|[Ff]icha[ _]de[ _][Mm]úsico|[Ff]icha[ _]de[ _][Cc]antante|[Ii]nfobox[ _][Mm]usical[ _][Aa]rtist)([\s_]*[}\|])', ur'{{ficha de artista musical\2'),
        # Pasar a {{ficha de taxón}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Tt]axobox[ _][Dd][ée]but|[Ff]icha[ _]de[ _]taxon|[Ff]icha[ _]de[ _][Vv]irus|[Tt]axobox)([\s_]*[}\|])', ur'{{ficha de taxón\2'),
        # Pasar a {{ficha de organización}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Ii]nfobox[ _][Cc]ompany|[Ii]nfobox[ _][Ee]mpresa|[Ii]nfobox[ _][Ee]mpresa[ _][Dd]esaparecida|[Ii]nfobox[ _][Oo]rganizaci[óo]n|[Ff]icha[ _]de[ _]ONG|[Ff]icha[ _]de[ _]empresa|[Ff]icha[ _]de[ _]asociaci[óo]n|[Ii]nfobox[ _][Oo]rganization|[Ff]icha[ _]de[ _]Organizaci[óo]n|[Ff]icha[ _]de[ _][Ff][áa]brica)([\s_]*[}\|])', ur'{{ficha de organización\2'),
        # Pasar a {{ficha de sencillo}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Ii]nfobox[ _][Ss]ingle)([\s_]*[}\|])', ur'{{ficha de sencillo\2'),
        # Pasar a {{ficha de canción}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Cc]anci[óo]n|[Ff]icha[ _]de[ _][Cc]ancion|[Ff]icha[ _]de[ _]Canción)([\s_]*[}\|])', ur'{{ficha de canción\2'),
        # Pasar a {{ficha de canal de televisión}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Ii]nfobox[ _][Cc]anal[ _]de[ _]TV|[Tt]elevisora|[Ff]icha[ _]de[ _]televisora|[Ff]icha[ _]de[ _]canal[ _]de[ _]television|[Ii]nfobox[ _]TV[ _]channel)([\s_]*[}\|])', ur'{{ficha de canal de televisión\2'),
        # Pasar a {{ficha de persona}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Ii]nfobox[ _][Bb]iograf[íi]a|[Ff]icha[ _]de[ _][Bb]iograf[íi]a|[Ii]nfobox[ _][Pp]ersonalidades)([\s_]*[}\|])', ur'{{ficha de persona\2'),
        # Pasar a {{ficha de película}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Ii]nfobox[ _][Pp]el[íi]cula|[Ff]icha[ _]de[ _][Cc]ortometraje|[Ff]icha[ _]de[ _][Pp]elicula)([\s_]*[}\|])', ur'{{ficha de película\2'),
        # Pasar a {{ficha de localidad de Japón}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Ii]nfobox[ _][Cc]iudad[ _][Jj]ap[oó]n)([\s_]*[}\|])', ur'{{ficha de localidad de Japón\2'),
        # Pasar a {{ficha de localidad de Brasil}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Ii]nfobox[ _][Cc]iudad[ _][Bb]rasil)([\s_]*[}\|])', ur'{{ficha de localidad de Brasil\2'),
        # Pasar a {{ficha de localidad de Cuba}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Ii]nfobox[ _][Cc]iudad[ _][Cc]uba)([\s_]*[}\|])', ur'{{ficha de localidad de Cuba\2'),
        # Pasar a {{ficha de localidad de Uruguay}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Ii]nfobox[ _][Cc]iudad[ _][Uu]ruguay)([\s_]*[}\|])', ur'{{ficha de localidad de Uruguay\2'),
        # Pasar a {{ficha de localidad de Estonia}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Ii]nfobox[ _][Ll]inn)([\s_]*[}\|])', ur'{{ficha de localidad de Estonia\2'),
        # Pasar a {{ficha de localidad de Polonia}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Ii]nfobox[ _][Pp]olonia)([\s_]*[}\|])', ur'{{ficha de localidad de Polonia\2'),
        # Pasar a {{leyenda}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Ll]egend|[Ll]egend3)([\s_]*[}\|])', ur'{{leyenda\2'),
        # Pasar a {{ficha de escultismo}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Ii]nfobox[ _][Ee]scultismomundial)([\s_]*[}\|])', ur'{{ficha de escultismo\2'),
        # Pasar a {{etiqueta imagen}} y similares
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Ii]mage[ _]label[ _]*\|([^}]*)}}', ur'{{etiqueta imagen|\1}}'),
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Ii]mage[ _]label[ _]begin[ _]*\|([^}]*)}}', ur'{{etiqueta imagen inicio|\1}}'),
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Ii]mage[ _]label[ _]small[ _]*\|([^}]*)}}', ur'{{etiqueta imagen pequeña|\1}}'),
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Ii]mage[ _]label[ _]end[ _]*\|([^}]*)}}', ur'{{etiqueta imagen fin|\1}}'),
        # Pasar a {{referencias}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Rr]efs|[Uu]nreferenced|[Rr]efimprove|[Uu]nsourced)(\s*[}\|])', ur'{{referencias\2'),
        # Pasar a {{copyedit}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Oo]rtografía|[Gg]ramática)(\s*[}\|])', ur'{{copyedit\2'),
        # Pasar a {{otros usos}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Oo]trosusos|[Oo]theruses|[Oo]theruses4|[Ss]obre|[Pp]ara)(\s*[}\|])', ur'{{otros usos\2'),
        # Pasar a {{distinguir}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Cc]onfusión|[Nn]o\sconfundir)(\s*[}\|])', ur'{{distinguir\2'),
        # Pasar a {{desambiguación}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Dd]esambig|[Dd]es|[Dd]esambiguacion|[Dd]isambig)(\s*[}\|])', ur'{{desambiguación\2'),
        # Pasar a {{listaref}}
        (ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Rr]ef(?:erences|list)(\s*[}\|])', ur'{{listaref\1'),

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
            ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*([Cc]ita'
                                                                     ur'|[Qq]uote'
                                                                     ur'|[Cc]quote'
                                                                     ur'|[Qq]uotation'
                                                                     ur'|[Zz]itat)[\s_]*\|.+?}}',
            ur'{{[^}]+?\|[\s_]*(cita|quote|quotation)[\s_]*=.+?(}}|\|)',
            # Títulos, por falsos positivos
            ur'\|\s*(title|t[íi]tulo)\s*=\s*[^\]\|]*?[\]\|]',
            # Minúsculas inciertas en meses
            ur'(?i)(acuerdo'
                ur'|decreto'
                ur'|ley'
                ur'|norma(tiva)?'
                ur'|[óo]rden'
                ur'|procedimiento'
                ur'|resoluci[óo]n) +del? +\d\d? +del? +\S\S',
            # Parámetros de {{cita web}} inseguros
            ur'{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Rr]ef[-](internet|web)[^}]*(?:[Aa]lias\d?'
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
                                                                                                   ur'|[Vv][íi]nculo ?autor\d)\s*=.*?[|}]',
            # No editar si el artículo contiene determinadas plantillas
                # Artículos cuya edición por bots queda prohibida según
                # [[w:es:WP:PBOT#R9.3]]
                ur'.*{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Nn]obots[\s_]*[|}].*',
                # Artículos en desarrollo activo
                ur'.*{{[\s_]*(?:[Pp]lantilla[\s_]*:|[Tt]emplate[\s_]*:)?[\s_]*[Ee]n[ _]?uso[\s_]*[|}].*',
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
