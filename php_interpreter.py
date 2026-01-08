import re

class MiniPHPInterpreter:
    def __init__(self):
        self.vars = {}
        self.output = []

    def execute(self, code):
        lines = [l.strip() for l in code.splitlines() if l.strip()]
        i = 0

        while i < len(lines):
            line = lines[i]

            # assignment luar IF
            if line.startswith("$") and "=" in line:
                self._handle_assignment(line)

            elif line.startswith("IF"):
                cond = re.search(r"\((.*?)\)", line).group(1)
                left, right = cond.replace("$", "").split(">")
                condition = self.vars["$"+left.strip()] > self.vars["$"+right.strip()]

                i += 1
                if condition:
                    while not lines[i].startswith("}"):
                        self._execute_line(lines[i])
                        i += 1
                    i += 1
                    while not lines[i].startswith("}"):
                        i += 1
                else:
                    while not lines[i].startswith("ELSE"):
                        i += 1
                    i += 2
                    while not lines[i].startswith("}"):
                        self._execute_line(lines[i])
                        i += 1
            i += 1

        return "\n".join(self.output)

    def _execute_line(self, line):
        # assignment di dalam block
        if line.startswith("$") and "=" in line:
            self._handle_assignment(line)

        elif line.startswith("PRINT"):
            text = line.replace("PRINT", "").replace(";", "")
            parts = text.split(".")
            result = ""
            for p in parts:
                p = p.strip()
                if p.startswith("$"):
                    result += str(self.vars.get(p, ""))
                else:
                    result += p.replace('"', '')
            self.output.append(result)

    def _handle_assignment(self, line):
        var, val = line.replace(";", "").split("=")
        var = var.strip()
        val = val.strip()
        if val.startswith("$"):
            self.vars[var] = self.vars[val]
        else:
            self.vars[var] = int(val)
