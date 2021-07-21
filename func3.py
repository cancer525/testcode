@icemac.addressbook.utils.set_site
def principal_id_to_title(id, context):
    "Convert a principal id into its title."
    auth = zope.component.getUtility(
        zope.authentication.interfaces.IAuthentication)
    try:
        principal = auth.getPrincipal(id)
    except zope.authentication.interfaces.PrincipalLookupError:
        return id
    else:
        return principal.title


def update_object(obj, context):
    "Update one object."
    creators = zope.dublincore.interfaces.IZopeDublinCore(obj).creators
    if not len(creators):
        return
    editor_storage = icemac.addressbook.metadata.interfaces.IEditor(obj)
    editor_storage.creator = principal_id_to_title(context, creators[0], obj)
    editor_storage.modifier = principal_id_to_title(context, creators[-1], obj)

