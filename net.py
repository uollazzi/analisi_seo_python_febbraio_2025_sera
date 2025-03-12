r = {
    "nmap": {
        "command_line": "nmap -oX - -p 80,443,21,23,22,17988 -sV 127.0.0.1",
        "scaninfo": {"tcp": {"method": "connect", "services": "21-23,80,443,17988"}},
        "scanstats": {
            "timestr": "Mon Mar 10 16:38:43 2025",
            "elapsed": "0.32",
            "uphosts": "1",
            "downhosts": "0",
            "totalhosts": "1",
        },
    },
    "scan": {
        "127.0.0.1": {
            "hostnames": [{"name": "localhost", "type": "PTR"}],
            "addresses": {"ipv4": "127.0.0.1"},
            "vendor": {},
            "status": {"state": "up", "reason": "conn-refused"},
            "tcp": {
                21: {
                    "state": "closed",
                    "reason": "conn-refused",
                    "name": "ftp",
                    "product": "",
                    "version": "",
                    "extrainfo": "",
                    "conf": "3",
                    "cpe": "",
                },
                22: {
                    "state": "closed",
                    "reason": "conn-refused",
                    "name": "ssh",
                    "product": "",
                    "version": "",
                    "extrainfo": "",
                    "conf": "3",
                    "cpe": "",
                },
                23: {
                    "state": "closed",
                    "reason": "conn-refused",
                    "name": "telnet",
                    "product": "",
                    "version": "",
                    "extrainfo": "",
                    "conf": "3",
                    "cpe": "",
                },
                80: {
                    "state": "closed",
                    "reason": "conn-refused",
                    "name": "http",
                    "product": "",
                    "version": "",
                    "extrainfo": "",
                    "conf": "3",
                    "cpe": "",
                },
                443: {
                    "state": "closed",
                    "reason": "conn-refused",
                    "name": "https",
                    "product": "",
                    "version": "",
                    "extrainfo": "",
                    "conf": "3",
                    "cpe": "",
                },
                17988: {
                    "state": "closed",
                    "reason": "conn-refused",
                    "name": "",
                    "product": "",
                    "version": "",
                    "extrainfo": "",
                    "conf": "",
                    "cpe": "",
                },
            },
        }
    },
}

# <h2>HOST: 127.0.0.1</h2>
#       <table>
#         <thead>
#           <th>Port</th>
#           <th>Status</th>
#         </thead>
#         <tbody>
#           <tr>
#             <td>21</td>
#             <td>closed</td>
#           </tr>
#           <tr>
#             <td>22</td>
#             <td>opened</td>
#           </tr>
#         </tbody>
#       </table>
html = ""

for host in r["scan"].items():
    # host in quanto ITEM del DICT r["scan"] è SEMPRE una TUPLA di 2 elementi
    html += f"<h2>HOST: {host[0]}</h2>"
    html += """
    <table class="table table-hover">
        <thead>
          <th>Port</th>
          <th>Status</th>
        </thead>
        <tbody>
    """

    tcps = host[1]["tcp"]

    for port in tcps.items():
        # port in quanto ITEM del DICT tcps è SEMPRE una TUPLA di 2 elementi
        html += f"""<tr>
            <td>{port[0]}</td>
            <td>{port[1]["state"]}</td>
          </tr>"""

    html += """
    </tbody>
      </table>
    """

template_html = ""
with open("scan_template.html", "rt", encoding="utf8") as f:
    template_html = f.read()

template_html = template_html.replace("%%SCAN%%", html)

with open("scan.html", "wt", encoding="utf8") as f:
    f.write(template_html)
