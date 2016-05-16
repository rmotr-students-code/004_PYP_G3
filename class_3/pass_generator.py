class PasswordGenerator(object):
    
    def __init__(self):
        self.generated_passwords = set()

    def __iter__(self):
        return self

    def _generate_password(self):
        # This has the magic
        pass

    def __next__(self):
        pwd = self._generate_password()
        already_generated = pwd in self.generated_passwords
        while already_generated:
            pwd = self._generate_password()

        return pwd


pass_gen = PasswordGenerator()

for pwd in pass_gen:
    user.pwd = pwd
    
for pwd in pass_gen:
    admin.pwd = pwd
