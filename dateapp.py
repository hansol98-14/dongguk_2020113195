def save(self):
    """ save """
    with open(self.filename, 'wb') as file_handle:
        pickle.dump(self.info, file_handle) # save


cnt = int(input('운동횟수를 입력해주세요'))
cnt.save()
