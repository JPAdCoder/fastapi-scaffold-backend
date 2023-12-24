"""
Time ${time}
Author ${author}
Email ${email}
"""

% for v in import_pkg_list:
% if v["from"]:
from ${v["from"]} import ${v["import"]}
% else:
import ${v["import"]}
% endif
% endfor


% for schema_class in schema_classes:
class ${schema_class["name"]}(${schema_class["parent_class"]}):
    % if schema_class["is_pass"]:
    pass
    % else:
    % for v in schema_class["fields"]:
    % if v["optional"]:
    ${v["field_name"]}: Optional[${v["field_type"]}] = Field(
    % else:
    ${v["field_name"]}: ${v["field_type"]} = Field(
    % endif
        % for attr in v["attrs"]:
        % if attr["attr_name"] is not None:
        ${attr["attr_name"]}=${attr["attr_value"]},
        % else:
        ${attr["attr_value"]},
        % endif
        % endfor
    )
    % endfor
    % if schema_class["meta_class"] is not None:

    class ${schema_class["meta_class"]["name"]}:
        % for m_f in schema_class["meta_class"]["fields"]:
        ${m_f["name"]} = ${m_f["value"]}
        % endfor
    % else:
    % endif
    % endif


% endfor
