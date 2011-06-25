from quickpages.utils.minitags import script, tag1

def jstags (flist):
    return '\n'.join ([script ('', type="text/javascript", src="'" + j + '"') for j in flist])

def csstags (flist):
    return '\n'.join ([tag1 ('link', rel="stylesheet", type='text/css', href='"' + f + '"') for f in flist])
