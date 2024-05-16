FROM alpine
ARG ARG_LICZBA="1000"
ARG ARG_USERNAME="Maciek"
ENV ENV_USERNAME=$ARG_USERNAME

WORKDIR /root

RUN echo -e "#!/bin/sh                        \n \
echo ---Zmienne na etapie budowania obrazu--- \n \
echo ENV_USERNAME=$ENV_USERNAME               \n \
echo ARG_LICZBA=$ARG_LICZBA                   \n \
echo ---Aktualne wartości zmiennych---" > test.sh

RUN echo 'echo ENV_USERNAME=$ENV_USERNAME' >> test.sh
RUN echo 'echo ARG_LICZBA=$ARG_LICZBA' >> test.sh
RUN chmod +x test.sh
ENTRYPOINT /bin/sh
