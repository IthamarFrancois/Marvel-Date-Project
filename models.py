## Referencing "pet_pals" code structure from professor Vikas Pandey's sample program.

def create_classes(db):
    class Marvel(db.Model):
        ## Name of local postgres table name
        __tablename__ = 'marvel_us_iitem'

        ## Represents the columns in dataset
        _id = db.Column(db.String, primary_key=True)
        TARGET = db.Column(db.String(200))
        CODENAME = db.Column(db.String(200))
        REAL_NAME = db.Column(db.String(200))
        GENDER = db.Column(db.String(20))
        RELATIONSHIP_STATUS = db.Column(db.String(20))
        ALIGNMENT = db.Column(db.String(20))
        HEIGHT = db.Column(db.String(20))
        WEIGHT = db.Column(db.String(20))
        EYECOLOR = db.Column(db.String(20))
        HAIRCOLOR = db.Column(db.String(20))
        IDENTIFIES_AS = db.Column(db.String(20))
        BIRTHPLACE = db.Column(db.String(20))
        CITIZENSHIP = db.Column(db.String(20))
        EDUCATION = db.Column(db.String(1000))
        EXPERIENCE = db.Column(db.String(1000))
        INTELLIGENCE = db.Column(db.Float)
        STRENGTH = db.Column(db.Float)
        SPEED = db.Column(db.Float)
        DURABILITY = db.Column(db.Float)
        ENERGY = db.Column(db.Float)
        FIGHTING = db.Column(db.Float)
        PROFILE_PIC = db.Column(db.String(255))
        FAVORITE_HANGOUTS = db.Column(db.String(1000))
        DETAILED_FILE = db.Column(db.String(1000))
        POWERS_URL = db.Column(db.String(1000))
        City = db.Column(db.String(20))
        State = db.Column(db.String(20))
        Zip_Code = db.Column(db.Integer)
        Latitude = db.Column(db.Float)
        Longitude = db.Column(db.Float)

        ## Returns column data for each row to 'app.py'
        def __repr__(self):
            return '<Marvel %r>' % (
                self._id, self.TARGET, self.CODENAME, self.REAL_NAME, self.GENDER, self.RELATIONSHIP_STATUS,
                self.ALIGNMENT, self.HEIGHT, self.WEIGHT, self.EYECOLOR, self.HAIRCOLOR, self.IDENTIFIES_AS,
                self.BIRTHPLACE, self.CITIZENSHIP, self.EDUCATION, self.EXPERIENCE, self.INTELLIGENCE, self.STRENGTH,
                self.SPEED, self.DURABILITY, self.ENERGY, self.FIGHTING, self.PROFILE_PIC, self.FAVORITE_HANGOUTS,
                self.DETAILED_FILE, self.POWERS_URL, self.City, self.State, self.Zip_Code, self.Latitude, self.Longitude
                )
    return Marvel
