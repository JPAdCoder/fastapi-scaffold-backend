"""
Time ${time}
Author ${author}
Email ${email}
"""

% for v in merged_import_pkg_list:
% if v["from"]:
from ${v["from"]} import ${v["import"]}
% else:
import ${v["import"]}
% endif
% endfor

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=${engine["pool_pre_ping"]}, pool_recycle=${engine["pool_recycle"]}, pool_size=${engine["pool_size"]})
SessionLocal = sessionmaker(autocommit=${session_local["autocommit"]}, autoflush=${session_local["autoflush"]}, bind=engine, expire_on_commit=${session_local["expire_on_commit"]})