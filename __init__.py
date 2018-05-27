from antlr4 import *
from .TSqlParser import TSqlParser
from .TSqlLexer import *
from .TSqlParserListener import TSqlParserListener
import sys, re
from collections import defaultdict

refunc = re.compile("^(enter|exit)")
def getfunc(frame):
    return refunc.sub("", frame.f_code.co_name)

KEYWORDS = ["ABSOLUTE","ACTION","ADA","ADD","ADMIN","AFTER","AGGREGATE","ALIAS","ALL","ALLOCATE","ALTER","AND","ANY","ARE","ARRAY","AS","ASC","ASENSITIVE","ASSERTION","ASYMMETRIC","AT","ATOMIC","AUTHORIZATION","AVG","BACKUP","BEFORE","BEGIN","BETWEEN","BINARY","BIT","BIT_LENGTH","BLOB","BOOLEAN","BOTH","BREADTH","BREAK","BROWSE","BULK","BY","CALL","CALLED","CARDINALITY","CASCADE","CASCADED","CASE","CAST","CATALOG","CHAR","CHARACTER","CHARACTER_LENGTH","CHAR_LENGTH","CHECK","CHECKPOINT","CLASS","CLOB","CLOSE","CLUSTERED","COALESCE","COLLATE","COLLATION","COLLECT","COLUMN","COMMIT","COMPLETION","COMPUTE","CONDITION","CONNECT","CONNECTION","CONSTRAINT","CONSTRAINTS","CONSTRUCTOR","CONTAINS","CONTAINSTABLE","CONTINUE","CONVERT","CORR","CORRESPONDING","COUNT","COVAR_POP","COVAR_SAMP","CREATE","CROSS","CUBE","CUME_DIST","CURRENT","CURRENT_CATALOG","CURRENT_DATE","CURRENT_DEFAULT_TRANSFORM_GROUP","CURRENT_PATH","CURRENT_ROLE","CURRENT_SCHEMA","CURRENT_TIME","CURRENT_TIMESTAMP","CURRENT_TRANSFORM_GROUP_FOR_TYPE","CURRENT_USER","CURSOR","CYCLE","DATA","DATABASE","DATE","DAY","DBCC","DEALLOCATE","DEC","DECIMAL","DECLARE","DEFAULT","DEFERRABLE","DEFERRED","DELETE","DENY","DEPTH","DEREF","DESC","DESCRIBE","DESCRIPTOR","DESTROY","DESTRUCTOR","DETERMINISTIC","DIAGNOSTICS","DICTIONARY","DISCONNECT","DISK","DISTINCT","DISTRIBUTED","DOMAIN","DOUBLE","DROP","DUMP","DYNAMIC","EACH","ELEMENT","ELSE","END","END-EXEC","EQUALS","ERRLVL","ESCAPE","EVERY","EXCEPT","EXCEPTION","EXEC","EXECUTE","EXISTS","EXIT","EXTERNAL","EXTRACT","FALSE","FETCH","FILE","FILLFACTOR","FILTER","FIRST","FLOAT","FOR","FOREIGN","FORTRAN","FOUND","FREE","FREETEXT","FREETEXTTABLE","FROM","FULL","FULLTEXTTABLE","FUNCTION","FUSION","GENERAL","GET","GLOBAL","GO","GOTO","GRANT","GROUP","GROUPING","HAVING","HOLD","HOLDLOCK","HOST","HOUR","IDENTITY","IDENTITYCOL","IDENTITY_INSERT","IF","IGNORE","IMMEDIATE","IN","INCLUDE","INDEX","INDICATOR","INITIALIZE","INITIALLY","INNER","INOUT","INPUT","INSENSITIVE","INSERT","INT","INTEGER","INTERSECT","INTERSECTION","INTERVAL","INTO","IS","ISOLATION","ITERATE","JOIN","KEY","KILL","LANGUAGE","LARGE","LAST","LATERAL","LEADING","LEFT","LESS","LEVEL","LIKE","LIKE_REGEX","LIMIT","LINENO","LN","LOAD","LOCAL","LOCALTIME","LOCALTIMESTAMP","LOCATOR","LOWER","MAP","MATCH","MAX","MEMBER","MERGE","METHOD","MIN","MINUTE","MOD","MODIFIES","MODIFY","MODULE","MONTH","MULTISET","NAMES","NATIONAL","NATURAL","NCHAR","NCLOB","NEW","NEXT","NO","NOCHECK","NONCLUSTERED","NONE","NORMALIZE","NOT","NULL","NULLIF","NUMERIC","OBJECT","OCCURRENCES_REGEX","OCTET_LENGTH","OF","OFF","OFFSETS","OLD","ON","ONLY","OPEN","OPENDATASOURCE","OPENQUERY","OPENROWSET","OPENXML","OPERATION","OPTION","OR","ORDER","ORDINALITY","OUT","OUTER","OUTPUT","OVER","OVERLAPS","OVERLAY","PAD","PARAMETER","PARAMETERS","PARTIAL","PARTITION","PASCAL","PATH","PERCENT","PERCENTILE_CONT","PERCENTILE_DISC","PERCENT_RANK","PIVOT","PLAN","POSITION","POSITION_REGEX","POSTFIX","PRECISION","PREFIX","PREORDER","PREPARE","PRESERVE","PRIMARY","PRINT","PRIOR","PRIVILEGES","PROC","PROCEDURE","PUBLIC","RAISERROR","RANGE","READ","READS","READTEXT","REAL","RECONFIGURE","RECURSIVE","REF","REFERENCES","REFERENCING","REGR_AVGX","REGR_AVGY","REGR_COUNT","REGR_INTERCEPT","REGR_R2","REGR_SLOPE","REGR_SXX","REGR_SXY","REGR_SYY","RELATIVE","RELEASE","REPLICATION","RESTORE","RESTRICT","RESULT","RETURN","RETURNS","REVERT","REVOKE","RIGHT","ROLE","ROLLBACK","ROLLUP","ROUTINE","ROW","ROWCOUNT","ROWGUIDCOL","ROWS","RULE","SAVE","SAVEPOINT","SCHEMA","SCOPE","SCROLL","SEARCH","SECOND","SECTION","SECURITYAUDIT","SELECT","SEMANTICKEYPHRASETABLE","SEMANTICSIMILARITYDETAILSTABLE","SEMANTICSIMILARITYTABLE","SENSITIVE","SEQUENCE","SESSION","SESSION_USER","SET","SETS","SETUSER","SHUTDOWN","SIMILAR","SIZE","SMALLINT","SOME","SPACE","SPECIFIC","SPECIFICTYPE","SQL","SQLCA","SQLCODE","SQLERROR","SQLEXCEPTION","SQLSTATE","SQLWARNING","START","STATE","STATEMENT","STATIC","STATISTICS","STDDEV_POP","STDDEV_SAMP","STRUCTURE","SUBMULTISET","SUBSTRING","SUBSTRING_REGEX","SUM","SYMMETRIC","SYSTEM","SYSTEM_USER","TABLE","TABLESAMPLE","TEMPORARY","TERMINATE","TEXTSIZE","THAN","THEN","TIME","TIMESTAMP","TIMEZONE_HOUR","TIMEZONE_MINUTE","TO","TOP","TRAILING","TRAN","TRANSACTION","TRANSLATE","TRANSLATE_REGEX","TRANSLATION","TREAT","TRIGGER","TRIM","TRUE","TRUNCATE","TRY_CONVERT","TSEQUAL","UESCAPE","UNDER","UNION","UNIQUE","UNKNOWN","UNNEST","UNPIVOT","UPDATE","UPDATETEXT","UPPER","USAGE","USE","USER","USING","VALUE","VALUES","VARCHAR","VARIABLE","VARYING","VAR_POP","VAR_SAMP","VIEW","WAITFOR","WHEN","WHENEVER","WHERE","WHILE","WIDTH_BUCKET","WINDOW","WITH","WITHIN","WITHINGROUP","WITHOUT","WORK","WRITE","WRITETEXT","XMLAGG","XMLATTRIBUTES","XMLBINARY","XMLCAST","XMLCOMMENT","XMLCONCAT","XMLDOCUMENT","XMLELEMENT","XMLEXISTS","XMLFOREST","XMLITERATE","XMLNAMESPACES","XMLPARSE","XMLPI","XMLQUERY","XMLSERIALIZE","XMLTABLE","XMLTEXT","XMLVALIDATE","YEAR","ZONE"]

class ParserListener(TSqlParserListener):
    def __init__(self, sql, start="tsql_file"):
        self.sql = sql
        self.start = start
        self.lexer = TSqlLexer(InputStream(self.sql.upper()))
        self.parser = TSqlParser(CommonTokenStream(self.lexer))
        self.tree = self.parser.__getattribute__(start)()
        self.context = defaultdict(set)
        self._list = None
        self._index = None
    
    
    def tolist(self):
        if self._list is not None:
            return self._list
        
        lisp = self.tree.toStringTree(None, self.parser)
        r = re.sub(r' (<EOF>|;)', '', lisp).replace("(", '("').replace(" ", '",')
        r = re.sub(r"(,)([^,\(]+)", r'\1"\2', r)
        r = re.sub(r'([^"\)]+)\)', r'\1")', r).replace(')"', ')')
        r = re.sub(r'\("id",\("simple_id",("[^"]+")\)\)|\("(?:constant|queue_id|id)",("[^"]+")\)', r'\1\2', r)
#            r = re.sub(',("(\.|AS)")?,+', ",", r).replace(',"",', ",")
        r = re.sub(',("AS")?,+', ",", r).replace(',"",', ",")
        lst = eval(r.replace("(", "[").replace(")", "]").replace('],"]','],]'))
        while True:
            if len(lst) != 2:
#                    lst = lst[1:]
                self._list = lst
                return lst
            lst = lst[1]


    def lookup(self):
        if self._index is not None:
            return self._index
        
        ret = defaultdict(set)
        kw = []
        def enumlist(args):
            for i, key in enumerate(args):
                if any(isinstance(x, list) for x in key):
                    if isinstance(key[-1], str):
                        if len(key[1]) == 2:
                            ret[key[0]].add("".join(key[1][1:] + key[2:]))
                    elif isinstance(key[1], str) and key[1] not in KEYWORDS:
                        ret[key[0]].add(key[1])
        
                    enumlist(key)
                elif isinstance(key,list):
                    if len(key) == 2:
                        ret[key[0]].add(key[1])
                    else:
                        ret[key[0]].add("".join(key[1:]))
                elif key in KEYWORDS:
                    kw.append(key)
        ret["keywords"] = kw
        enumlist(self.tolist())
        return dict((x,list(ret[x])) for x in ret)
    
    
    def __getattr__(self, name):
        try:
            return self.lookup()[name]
        except KeyError:
            raise AttributeError("No Such Attributes.\n\tExample Analized attributes\n\t\t'{}'".format("' or\n\t\t'".join(self.lookup().keys())))

    def __dir__(self):
        return super().__dir__() + list(self.lookup().keys())

def parse(sql, start="tsql_file", callback=ParserListener):
    listener = callback(sql, start)
    ParseTreeWalker().walk(listener, listener.tree)
    return listener