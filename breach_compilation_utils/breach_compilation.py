from pathlib import Path
import chardet


class BreachCompilation:

    def __init__(self, path):
        self.root_path = path

    def _iter_file(self, p):
        if p.is_file():
            if p.name != "symbols":
                yield p
        elif p.is_dir():
            for x in p.iterdir():
                yield from self._iter_file(x)

    def _mk_cred(self, line):
        url, *pwd = line.split(":")
        return url, ':'.join(pwd)

    def _iter_one_file(self, fname):
        print("Iter file:", fname)
        with open(fname, "rb") as file:
            raw = file.read()
            for raw_line in raw.split(b"\n"):
            #while 1:
                #raw_line = file.readline()[:-1]
                try:
                    line = raw_line.decode("utf-8")
                except UnicodeDecodeError:
                    c = chardet.detect(raw_line)
                    enc = c['encoding']
                    #print("Raw: ", raw_line, " to:", enc)
                    try:
                        if enc:
                            line = raw_line.decode(c["encoding"])
                        else:
                            continue
                    except UnicodeDecodeError:
                        continue
                    except LookupError:
                        continue
                if line:
                    yield self._mk_cred(line)
                else:
                    break

    def iter_credentials(self):
        for file in self._iter_file(Path(self.root_path)):
            yield from self._iter_one_file(file)

    def iter_email(self, email):
        cur_p = Path(self.root_path)
        for c in email:
            if (cur_p / c).exists():
                cur_p = cur_p / c
            else:
                break
        for login, pwd in self._iter_one_file(cur_p):
            if login.startswith(email):
                yield login, pwd

    def email_exists(self, email):
        for _, _ in self.iter_email(email):
            return True
        return False
