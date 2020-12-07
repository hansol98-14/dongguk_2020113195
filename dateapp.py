def save(self):
    """ save """
    with open(self.filename, 'wb') as file_cnt:
        pickle.dump(self.info, file_cnt) # save


cnt = int(input('운동횟수를 입력해주세요'))
cnt.save()
