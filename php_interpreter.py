class MiniPHPInterpreter:
    def __init__(self):
        self.vars = {}
        self.output = []

    def execute(self, code: str) -> str:
        self.vars = {}
        self.output = []

        lines = [
            line.strip()
            for line in code.splitlines()
            if line.strip()
            and not line.strip().startswith("<?")
            and not line.strip().startswith("?>")
        ]

        i = 0
        while i < len(lines):
            line = lines[i]

            # IF condition
            if line.upper().startswith("IF"):
                condition = line[2:].strip().lstrip("(").rstrip(") {")
                left, op, right = condition.split()

                left_val = self.vars.get(left, 0)
                right_val = self.vars.get(right, 0)

                condition_result = False
                if op == ">":
                    condition_result = left_val > right_val
                elif op == "<":
                    condition_result = left_val < right_val
                elif op == "==":
                    condition_result = left_val == right_val

                i += 1

                if condition_result:
                    # execute IF block
                    while i < len(lines) and not lines[i].startswith("}"):
                        self._execute_line(lines[i])
                        i += 1

                    i += 1  # skip }

                    # skip ELSE block if exists
                    if i < len(lines) and lines[i].upper().startswith("ELSE"):
                        i += 1
                        while i < len(lines) and not lines[i].startswith("}"):
                            i += 1
                        i += 1
                else:
                    # skip IF block
                    while i < len(lines) and not lines[i].startswith("}"):
                        i += 1
                    i += 1

                    # execute ELSE block
                    if i < len(lines) and lines[i].upper().startswith("ELSE"):
                        i += 1
                        while i < len(lines) and not lines[i].startswith("}"):
                            self._execute_line(lines[i])
                            i += 1
                        i += 1

            else:
                self._execute_line(line)
                i += 1

        return "\n".join(self.output)

    def _execute_line(self, line: str):
        line = line.strip()

        # Variable assignment
        if line.startswith("$") and "=" in line:
            var, val = line.split("=", 1)
            var = var.strip()
            val = val.replace(";", "").strip()

            if val.isdigit():
                self.vars[var] = int(val)
            elif val.startswith("$"):
                self.vars[var] = self.vars.get(val, 0)
            else:
                self.vars[var] = val.replace('"', "")

        # PRINT statement
        elif line.upper().startswith("PRINT"):
            content = line[5:].replace(";", "").strip()
            parts = content.split(".")
            result = ""

            for p in parts:
                p = p.strip()
                if p.startswith("$"):
                    result += str(self.vars.get(p, 0))
                else:
                    result += p.replace('"', "")

            self.output.append(result)
