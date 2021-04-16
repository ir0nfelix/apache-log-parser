FROM python:3.8-slim

RUN  groupadd -r -g 777 django && useradd django -u 777 -g django

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y wget gnupg2

RUN wget -O- https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y apt-transport-https curl bzip2 cron distro-info-data exim4-base exim4-config exim4-daemon-light \
    file guile-2.2-libs krb5-locales libbsd0 libc-l10n libedit2 libevent-2.1-6 libfribidi0 libgc1c2 libgnutls-dane0 \
    libgpm2 libgsasl7 libgssapi-krb5-2 libicu63 libidn11 libk5crypto3 libkeyutils1 libkrb5-3 libkrb5support0 \
    libkyotocabinet16v5 libldap-2.4-2 libldap-common libllvm7 libltdl7 liblzo2-2 libmagic-mgc libmagic1 libmailutils5 \
    libmariadb3 libmpdec2 libncurses6 libntlm0 libpopt0 libpq5 libprocps7 libpython2.7 libpython2.7-minimal \
    libpython2.7-stdlib libpython3-stdlib libpython3.7-minimal libpython3.7-stdlib libsasl2-2 libsasl2-modules \
    libsasl2-modules-db libsensors-config libsensors5 libunbound8 libwrap0 libxml2 libxslt1.1 locales logrotate \
    lsb-base lsb-release mailutils mailutils-common mariadb-common mime-support mysql-common \
    postgresql-client-12 procps psmisc sensible-utils \
    ssl-cert sysstat ucf xz-utils && \
    apt-get remove -y wget gnupg2 && apt-get autoremove -y && \
    apt-get clean && \
    update-ca-certificates && \
    pip3 install --upgrade pip setuptools && \
    ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime && dpkg-reconfigure -f noninteractive tzdata && \
    rm -r /root/.cache


RUN mkdir -p /django_application && mkdir -p /django_application/upload && chown -R django /django_application
WORKDIR /django_application

ADD ./requirements.txt /django_application
RUN pip3 install -r requirements.txt

COPY ./env.sh /env.sh
COPY ./start.sh /start.sh

ADD . /django_application/

EXPOSE 8000

CMD ["/start.sh"]
