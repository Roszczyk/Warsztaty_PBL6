package de.wwu.pi;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.ViewScoped;

import org.jboss.resteasy.client.jaxrs.ResteasyClientBuilder;
import org.jboss.resteasy.client.jaxrs.ResteasyWebTarget;
import org.jboss.resteasy.plugins.providers.RegisterBuiltin;
import org.jboss.resteasy.spi.ResteasyProviderFactory;

@ManagedBean
@ViewScoped
public class Client {

	private static final String BASE_URI_ADD = "http://add-server:8080/AddServer";
	private static final String BASE_URI_MULTIPLY = "http://multiply-server:8080/MultiplyServer";


	private int first;
	private int second;
	private Integer result;

	public int getFirst() {
		return first;
	}

	public void setFirst(int first) {
		this.first = first;
	}

	public int getSecond() {
		return second;
	}

	public void setSecond(int second) {
		this.second = second;
	}

	public Integer getResult() {
		return result;
	}

	public void add() {
		// has to be done at least once
		RegisterBuiltin.register(ResteasyProviderFactory.getInstance());

		ResteasyWebTarget target = new ResteasyClientBuilder().build().target(BASE_URI_ADD);
		RestAdderClient adderClient = target.proxy(RestAdderClient.class);
		result = adderClient.add(first, second);
	}

	public void multiply() {
		// has to be done at least once
		RegisterBuiltin.register(ResteasyProviderFactory.getInstance());

		ResteasyWebTarget target = new ResteasyClientBuilder().build().target(BASE_URI_MULTIPLY);
		RestMultiplierClient multiplierClient = target.proxy(RestMultiplierClient.class);
		result = multiplierClient.add(first, second);
	}
}
