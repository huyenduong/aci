import acitoolkit.acitoolkit as aci



#Login to APIC

description = ('Simple application that logs on to the APIC'
                   ' and create a tenant.')
creds = aci.Credentials('apic', description)
args = creds.get()
session = aci.Session(args.url, args.login, args.password)
resp = session.login()
if not resp.ok:
    print('%% Could not login to APIC')

# Create a tenant
tenant = aci.Tenant('Pepsi')

# Push the tenant to the APIC
resp = session.push_to_apic(tenant.get_url(),
                                tenant.get_json())
if not resp.ok:
    print('%% Error: Could not push configuration to APIC')
    print(resp.text)