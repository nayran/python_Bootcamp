class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def when(self, location):
        final = self.df[self.df['City'] == location]['Year']
        final = list(final.drop_duplicates())
        print(final)
        return final

    def where(self, date):
        final = self.df[self.df['Year'] == date]['City']
        final = list(final.drop_duplicates())
        print(final)
        return final
